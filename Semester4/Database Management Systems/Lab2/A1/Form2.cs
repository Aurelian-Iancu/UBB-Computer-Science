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
using System.Configuration;

namespace A1
{
    public partial class Form2 : Form
    {
        private SqlConnection dbConnection;
        private SqlDataAdapter daParent, daChild;
        private DataSet tableData;
        private DataRelation drParentChild;
        BindingSource bsParent, bsChild;
        private List<TextBox> textBoxes;

        public Form2()
        {
            textBoxes = new List<TextBox> ();
            InitializeComponent();
            loadTextboxes();
        }

        private void ReloadEmployeesTableView()
        {
            
            string childTable = ConfigurationManager.AppSettings["ChildTableName"];
            if (tableData.Tables[childTable] != null)
                tableData.Tables[childTable].Clear();

            daChild.Fill(tableData, childTable);
            dgChild.DataSource = bsChild;
        }

        private void ParentView_SelectionChanged(object sender, EventArgs e)
        {
            
            if (dgParent.SelectedRows.Count != 0)
            {
                DataGridViewRow selectedRow = dgParent.SelectedRows[0];
                daChild.SelectCommand = new SqlCommand("Select * FROM " +
                    ConfigurationManager.AppSettings["ChildTableName"] +
                    " WHERE " + ConfigurationManager.AppSettings["ParentId"] + "=" + selectedRow.Cells[0].Value, dbConnection);
                ReloadEmployeesTableView();
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

        /*private void loadTextboxes()
        {
            try
            {
                // We create a list of strings which contains the columnNames
                // The columnNames are splitted by ','
                List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                // We fix 2 points for X and Y, in order to place the textBoxes
                int pointX = 170;
                int pointY = 410;

                ////We take the number of columns and we clear the panel, before placing the new textBoxes
                //int numberOfColumns = Convert.ToInt32(ConfigurationManager.AppSettings["NumberOfColumns"]);
                panel.Controls.Clear();

                foreach (string columnName in ColumnNames)
                {
                    // We create a new textbox
                    TextBox a = new TextBox();
                    textBoxes.Add(a);
                    a.Text = columnName;
                    a.Name = columnName;
                    a.Location = new Point(pointX, pointY);
                    a.Visible = true;
                    a.Parent = panel;
                    panel.Show();
                    pointY -= 30;
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
            }

        }*/

        private void loadTextboxes()
        {
            try
            {
                // We create a list of strings which contains the columnNames
                // The columnNames are splitted by ','
                List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                // We fix 2 points for X and Y, in order to place the textBoxes
                int pointX = 170;
                int pointY = 410;

                // We take the number of columns and we clear the panel, before placing the new controls
                panel.Controls.Clear();

                foreach (string columnName in ColumnNames)
                {
                    // We create a new label with the column name
                    Label label = new Label();
                    label.Text = columnName;
                    label.Name = columnName + "_label";
                    label.Location = new Point(pointX - 130, pointY + 5);
                    label.AutoSize = true;
                    label.Visible = true;
                    label.Parent = panel;

                    // We create a new textbox
                    TextBox textBox = new TextBox();
                    textBoxes.Add(textBox);
                    textBox.Name = columnName;
                    textBox.Location = new Point(pointX, pointY);
                    textBox.Visible = true;
                    textBox.Parent = panel;

                    panel.Show();
                    pointY -= 30;
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
            }
        }

        private void clearTextBoxes()
        {
            foreach (TextBox tb in textBoxes)
            {
                tb.Clear();
            }
        }


        private void reloadChildTableView()
        {
            string childTable = ConfigurationManager.AppSettings["ChildTableName"];
            if (tableData.Tables[childTable] != null)
                tableData.Tables[childTable].Clear();

            daChild.Fill(tableData, childTable);
            dgChild.DataSource = bsChild;

        }


        private void Form2_Load(object sender, EventArgs e)
        {
            dbConnection = new SqlConnection("Data Source = DESKTOP-RKNH9AP\\SQLEXPRESS;Initial Catalog=BeerStore; Integrated Security=True");
            dbConnection.Open();

            daParent = new SqlDataAdapter(ConfigurationManager.AppSettings["ParentSelectQuery"], dbConnection);
            tableData = new DataSet();
            daParent.Fill(tableData, ConfigurationManager.AppSettings["ParentTableName"]);
            dgParent.SelectionMode = DataGridViewSelectionMode.FullRowSelect;


            daChild = new SqlDataAdapter(ConfigurationManager.AppSettings["ChildSelectQuery"], dbConnection);
            daChild.Fill(tableData, ConfigurationManager.AppSettings["ChildTableName"]);
            dgChild.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            DataColumn storeIdStores = tableData.Tables[ConfigurationManager.AppSettings["ParentTableName"]].Columns[ConfigurationManager.AppSettings["ParentReferencedKey"]];
            DataColumn storeIdEmployees = tableData.Tables[ConfigurationManager.AppSettings["ChildTableName"]].Columns[ConfigurationManager.AppSettings["ParentReferencedKey"]];
            drParentChild = new DataRelation(ConfigurationManager.AppSettings["ForeingKey"], storeIdStores, storeIdEmployees);
            tableData.Relations.Add(drParentChild);

            bsParent = new BindingSource();
            bsParent.DataSource = tableData;
            bsParent.DataMember = ConfigurationManager.AppSettings["ParentTableName"];

            bsChild = new BindingSource();
            bsChild.DataSource = bsParent;
            bsChild.DataMember = ConfigurationManager.AppSettings["ForeingKey"];
            dgParent.DataSource = bsParent;
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            try
            {
                // We take the insert command
                string insertCommand = ConfigurationSettings.AppSettings["InsertQuery"];

                // We create the insert command
                this.daChild.InsertCommand = new SqlCommand(insertCommand, this.dbConnection);

                // We take the childTable's name
                string childTableName = ConfigurationManager.AppSettings["ChildTableName"];

                // We create a list with the column names of the child table which are splited by ','

                List<string> columnNamesList = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                // We go throguh all these columnNames
                // And then we parse the list of textBoxes in order to find the one whose name is the same as the columnName 
                foreach (string columnName in columnNamesList)
                {
                    foreach (TextBox tb in this.textBoxes)
                    {
                        if (tb.Name == columnName)
                        {
                            // After we find it, we insert to the coresponding parameter, the text from the textBox 
                            this.daChild.InsertCommand.Parameters.AddWithValue("@" + columnName, tb.Text);
                        }
                    }
                }

                // We open the connection and execute the query
                //this.dbConnection.Open();
                this.daChild.InsertCommand.ExecuteNonQuery();

                MessageBox.Show("Inserted with succes!");

                // We update the child table
                this.tableData = new DataSet();
                this.daChild.Fill(this.tableData, childTableName);
                this.dgChild.DataSource = this.tableData.Tables[childTableName];

                this.clearTextBoxes();

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                this.dbConnection.Close();
            }


        }



        private void removeButton_Click(object sender, EventArgs e)
        {
            string childId = ConfigurationManager.AppSettings["ChildId"];

            SqlCommand command = new SqlCommand("DELETE FROM " + ConfigurationManager.AppSettings["ChildTableName"] +
                " WHERE " + childId + "= @" + childId, dbConnection);

            foreach (TextBox tb in textBoxes)
            {
                if (tb.Name == childId)
                {
                    if (tb.Text.Length != 0)
                    {
                        int id = Int32.Parse(tb.Text);
                        command.Parameters.Add("@" + childId, SqlDbType.Int);
                        command.Parameters["@" + childId].Value = id;

                        try
                        {
                            daChild.DeleteCommand = command;
                            int numberofdeleted = daChild.DeleteCommand.ExecuteNonQuery();
                            if (numberofdeleted > 0)
                            {
                                MessageBox.Show("Deleted successfully!");
                                reloadChildTableView();
                            }
                            else
                            {
                                MessageBox.Show("No record with given id found!");
                            }
                        }
                        catch (SqlException ex)
                        {
                            MessageBox.Show(ex.ToString());
                        }
                    }
                    else
                    {
                        MessageBox.Show("Please input id");
                    }
                    break;
                }
            }
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                string updateCommand = ConfigurationManager.AppSettings["UpdateQuery"];

                this.daChild.UpdateCommand = new SqlCommand(updateCommand, this.dbConnection);

                string childTableName = ConfigurationManager.AppSettings["ChildTableName"];

                List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                foreach (string columnName in columnNames)
                {
                    foreach (TextBox tb in textBoxes)
                    {
                        if (tb.Name == columnName)
                        {
                            this.daChild.UpdateCommand.Parameters.AddWithValue("@" + columnName, tb.Text);
                        }
                    }
                }

                this.daChild.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated with success");

                this.tableData = new DataSet();
                this.daChild.Fill(this.tableData, childTableName);
                this.dgChild.DataSource = this.tableData.Tables[childTableName];

                foreach (TextBox tb in textBoxes)
                {
                    tb.Clear();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }
    }
}
