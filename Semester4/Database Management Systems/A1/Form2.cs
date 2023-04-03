using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace A1
{
    public partial class Form2 : Form
    {
        private SqlConnection dbConnection;
        private SqlDataAdapter daStores, daEmployees;
        private DataSet tableData;
        private DataRelation drStoresEmployees;
        BindingSource bsStores, bsEmployees;
        public Form2()
        {
            InitializeComponent();
        }

        private void ReloadEmployeesTableView()
        {
            if (tableData.Tables["Employees"] != null)
            {
                tableData.Tables["Employees"].Clear();
            }
            daEmployees.Fill(tableData, "Employees");
            EmployeesView.DataSource = bsEmployees;
        }

        private void StoresView_SelectionChanged(object sender, EventArgs e)
        {
            textBoxEmployeeId.Clear();
            textBoxStoreId.Clear();
            textBoxPositionId.Clear();
            textBoxName.Clear();
            if(StoresView.SelectedRows.Count != 0 ) {
                DataGridViewRow selectedRow = StoresView.SelectedRows[0];
                daEmployees.SelectCommand = new SqlCommand("Select * from Employees where stid = " + selectedRow.Cells[0].Value, dbConnection);
                ReloadEmployeesTableView();
            }
        }

        private void EmployeesView_SelectionChanged(Object sender, EventArgs e)
        {
            if(EmployeesView.SelectedRows.Count != 0) {
                DataGridViewRow selectedRow = EmployeesView.SelectedRows[0];
                textBoxEmployeeId.Text = selectedRow.Cells[0].Value.ToString();
                textBoxStoreId.Text = selectedRow.Cells[1].Value.ToString();
                textBoxPositionId.Text = selectedRow.Cells[2].Value.ToString();
                textBoxName.Text = selectedRow.Cells[3].Value.ToString();
            }
        }

        private void EmployeesView_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            if (e.Exception is InvalidConstraintException)
                MessageBox.Show("The store id you provided does not exist!");
            else if (e.Exception is FormatException)
                MessageBox.Show(e.Exception.Message);
            else
                try
                {
                    throw e.Exception;
                }
                catch (Exception ex) 
                {
                    MessageBox.Show(ex.ToString());
                }
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            dbConnection = new SqlConnection("Data Source = DESKTOP-RKNH9AP\\SQLEXPRESS;Initial Catalog=BeerStore; Integrated Security=True");
            dbConnection.Open();

            daStores = new SqlDataAdapter("select * from stores", dbConnection);
            tableData = new DataSet();
            daStores.Fill(tableData, "stores");
            StoresView.SelectionMode = DataGridViewSelectionMode.FullRowSelect;


            daEmployees = new SqlDataAdapter("select * from employees", dbConnection);
            daEmployees.Fill(tableData, "employees");
            EmployeesView.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            DataColumn storeIdStores = tableData.Tables["stores"].Columns["stid"];
            DataColumn storeIdEmployees = tableData.Tables["employees"].Columns["stid"];
            drStoresEmployees = new DataRelation("FK_STORE_EMPLOYEE", storeIdStores, storeIdEmployees);
            tableData.Relations.Add(drStoresEmployees);

            bsStores = new BindingSource();
            bsStores.DataSource = tableData;
            bsStores.DataMember = "Stores";

            bsEmployees = new BindingSource();
            bsEmployees.DataSource = bsStores;
            bsEmployees.DataMember = "FK_STORE_EMPLOYEE";
            StoresView.DataSource = bsStores;
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("INSERT INTO Employees (emid, stid, poid, name) values (@EmployeeId, @StoreId, @PositionId, @Name)", dbConnection);
            if (textBoxEmployeeId.Text.Length > 0)
            {
                try
                {
                    int employee_id = Int32.Parse(textBoxEmployeeId.Text);

                    if (textBoxStoreId.Text.Length > 0 && textBoxPositionId.Text.Length > 0)
                    {
                        int store_id = Int32.Parse(textBoxStoreId.Text);
                        int position_id = Int32.Parse(textBoxPositionId.Text);

                        command.Parameters.Add("@EmployeeId", SqlDbType.Int);
                        command.Parameters["@EmployeeId"].Value = employee_id;

                        command.Parameters.Add("@StoreId", SqlDbType.Int);
                        command.Parameters["@StoreId"].Value = store_id;

                        command.Parameters.Add("@PositionId", SqlDbType.Int);
                        command.Parameters["@PositionId"].Value = position_id;

                        command.Parameters.Add("@Name", SqlDbType.VarChar, 50);
                        command.Parameters["@Name"].Value = textBoxName.Text;
                        try
                        {
                            daEmployees.InsertCommand = command;
                            daEmployees.InsertCommand.ExecuteNonQuery();
                            ReloadEmployeesTableView();
                        }
                        catch (SqlException sqlException)
                        {
                            if (sqlException.Number == 2627)
                            {
                                MessageBox.Show("The employee id must be unique!");
                            }
                            else if (sqlException.Number == 547)
                            {
                                MessageBox.Show("There's no Store or Position with the give id");
                            }
                            else
                            {
                                MessageBox.Show(sqlException.Message);
                            }
                        }

                    }
                }
                catch (FormatException ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
            else
                MessageBox.Show("Please provide an employee id!");
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("DELETE FROM Employees WHERE emid = @EmployeeID", dbConnection);
            if (textBoxEmployeeId.Text.Length != 0)
            {
                int employee_id = Int32.Parse(textBoxEmployeeId.Text);
                command.Parameters.Add("@EmployeeID", SqlDbType.Int);
                command.Parameters["@EmployeeID"].Value = employee_id;
                try
                {
                    daEmployees.DeleteCommand = command;
                    int numberOfDeletedSingers = daEmployees.DeleteCommand.ExecuteNonQuery();
                    if (numberOfDeletedSingers == 0)
                    {
                        MessageBox.Show("There is no employee with the given id!");
                    }
                    else
                    {
                        ReloadEmployeesTableView();
                    }
                }
                catch (SqlException sqlException)
                {
                    MessageBox.Show(sqlException.ToString());
                }
            }
            else
                MessageBox.Show("Please provide an employee id!");
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("Update Employees " +
                "set emid = @EmployeeId, stid = @StoreId, poid = @PositionId, name = @Name" +
                " where emid = @EmployeeId", dbConnection);
            int employee_id = Int32.Parse(textBoxEmployeeId.Text);
            int store_id = Int32.Parse(textBoxStoreId.Text);
            int position_id = Int32.Parse(textBoxPositionId.Text);

            command.Parameters.Add("@EmployeeId", SqlDbType.Int);
            command.Parameters["@EmployeeId"].Value = employee_id;

            command.Parameters.Add("@StoreId", SqlDbType.Int);
            command.Parameters["@StoreId"].Value = store_id;

            command.Parameters.Add("@PositionId", SqlDbType.Int);
            command.Parameters["@PositionId"].Value = position_id;

            command.Parameters.Add("@Name", SqlDbType.VarChar, 50);
            command.Parameters["@Name"].Value = textBoxName.Text;

            try
            {
                daEmployees.UpdateCommand = command;
                int numberOfUpdatedEmployees = daEmployees.UpdateCommand.ExecuteNonQuery();
                if(numberOfUpdatedEmployees != 0)
                {
                    ReloadEmployeesTableView();
                }
                else
                {
                    MessageBox.Show("There is no employee with the given id!");
                }
            }
            catch(SqlException sqlException)
            {
                if (sqlException.Number == 2627)
                    MessageBox.Show("The employee id must be unique!");
                else if (sqlException.Number == 547)
                    MessageBox.Show("There's no store or position with the given id!");
                else
                    MessageBox.Show(sqlException.Message);
            }

        }
    }
}
