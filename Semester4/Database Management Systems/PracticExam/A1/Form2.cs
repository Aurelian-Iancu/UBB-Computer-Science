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
        private SqlDataAdapter daGroups, daChildren;
        private DataSet tableData;
        private DataRelation drGroupsChildren;
        BindingSource bsGroups, bsChildren;
        public Form2()
        {
            InitializeComponent();
        }

        private void ReloadChildrenTableView()
        {
            if (tableData.Tables["Children"] != null)
            {
                tableData.Tables["Children"].Clear();
            }
            daChildren.Fill(tableData, "Children");
            dgvChild.DataSource = bsChildren;
        }

        private void GroupsView_SelectionChanged(object sender, EventArgs e)
        {
            textBoxChildrenId.Clear();
            textBoxGroupId.Clear();
            textBoxName.Clear();
            textBoxSurname.Clear();
            textBoxGender.Clear();
            textBoxAge.Clear();
            if (dgvGroup.SelectedRows.Count != 0)
            {
                DataGridViewRow selectedRow = dgvGroup.SelectedRows[0];
                daChildren.SelectCommand = new SqlCommand("Select * from Children where gid = " + selectedRow.Cells[0].Value, dbConnection);
                ReloadChildrenTableView();
            }
        }

        private void ChildrenView_SelectionChanged(Object sender, EventArgs e)
        {
            if (dgvChild.SelectedRows.Count != 0)
            {
                DataGridViewRow selectedRow = dgvChild.SelectedRows[0];
                textBoxChildrenId.Text = selectedRow.Cells[0].Value.ToString();
                textBoxGroupId.Text = selectedRow.Cells[1].Value.ToString();
                textBoxName.Text = selectedRow.Cells[2].Value.ToString();
                textBoxSurname.Text = selectedRow.Cells[3].Value.ToString();
                textBoxGender.Text = selectedRow.Cells[4].Value.ToString();
                textBoxAge.Text = selectedRow.Cells[5].Value.ToString();
            }
        }

        private void ChildrenView_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            if (e.Exception is InvalidConstraintException)
                MessageBox.Show("The group id you provided does not exist!");
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
            dbConnection = new SqlConnection("Data Source = DESKTOP-RKNH9AP\\SQLEXPRESS;Initial Catalog=Practic; Integrated Security=True");
            dbConnection.Open();

            daGroups = new SqlDataAdapter("select * from groups", dbConnection);
            tableData = new DataSet();
            daGroups.Fill(tableData, "groups");
            dgvGroup.SelectionMode = DataGridViewSelectionMode.FullRowSelect;


            daChildren = new SqlDataAdapter("select * from children", dbConnection);
            daChildren.Fill(tableData, "children");
            dgvChild.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            DataColumn groupIdGroups = tableData.Tables["groups"].Columns["gid"];
            DataColumn groupIdChildren = tableData.Tables["children"].Columns["gid"];
            drGroupsChildren = new DataRelation("FK__Children__gid__3D5E1FD2", groupIdGroups, groupIdChildren);
            tableData.Relations.Add(drGroupsChildren);

            bsGroups = new BindingSource();
            bsGroups.DataSource = tableData;
            bsGroups.DataMember = "Groups";

            bsChildren = new BindingSource();
            bsChildren.DataSource = bsGroups;
            bsChildren.DataMember = "FK__Children__gid__3D5E1FD2";
            dgvGroup.DataSource = bsGroups;
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("INSERT INTO Children (cid, gid, name, surname, gender, age) values (@Cid, @Gid, @Name, @Surname, @Gender, @Age)", dbConnection);
            if (textBoxChildrenId.Text.Length > 0)
            {
                try
                {
                    int children_id = Int32.Parse(textBoxChildrenId.Text);

                    if (textBoxGroupId.Text.Length > 0 && textBoxName.Text.Length > 0)
                    {
                        int group_id = Int32.Parse(textBoxGroupId.Text);
                        //int position_id = Int32.Parse(textBoxName.Text);

                        command.Parameters.Add("@Cid", SqlDbType.Int);
                        command.Parameters["@Cid"].Value = children_id;

                        command.Parameters.Add("@Gid", SqlDbType.Int);
                        command.Parameters["@Gid"].Value = group_id;

                        command.Parameters.Add("@Surname", SqlDbType.VarChar, 50);
                        command.Parameters["@Surname"].Value = textBoxSurname.Text;

                        command.Parameters.Add("@Name", SqlDbType.VarChar, 50);
                        command.Parameters["@Name"].Value = textBoxName.Text;

                        command.Parameters.Add("@Gender", SqlDbType.VarChar, 50);
                        command.Parameters["@Gender"].Value = textBoxGender.Text;

                        int age = Int32.Parse(textBoxAge.Text);
                        command.Parameters.Add("@Age", SqlDbType.Int);
                        command.Parameters["@Age"].Value = age;

                        try
                        {
                            daChildren.InsertCommand = command;
                            daChildren.InsertCommand.ExecuteNonQuery();
                            ReloadChildrenTableView();
                        }
                        catch (SqlException sqlException)
                        {
                            if (sqlException.Number == 2627)
                            {
                                MessageBox.Show("The children id must be unique!");
                            }
                            else if (sqlException.Number == 547)
                            {
                                MessageBox.Show("There's no Group with the give id");
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
                MessageBox.Show("Please provide a children id!");
        }

        private void labelEmployees_Click(object sender, EventArgs e)
        {

        }

        private void dgv_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("DELETE FROM Children WHERE cid = @Cid", dbConnection);
            if (textBoxChildrenId.Text.Length != 0)
            {
                int children_id = Int32.Parse(textBoxChildrenId.Text);
                command.Parameters.Add("@Cid", SqlDbType.Int);
                command.Parameters["@Cid"].Value = children_id;
                try
                {
                    daChildren.DeleteCommand = command;
                    int numberOfDeletedChildren = daChildren.DeleteCommand.ExecuteNonQuery();
                    if (numberOfDeletedChildren == 0)
                    {
                        MessageBox.Show("There is no children with the given id!");
                    }
                    else
                    {
                        ReloadChildrenTableView();
                    }
                }
                catch (SqlException sqlException)
                {
                    MessageBox.Show(sqlException.ToString());
                }
            }
            else
                MessageBox.Show("Please provide a children id!");
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("Update Children " +
                "set cid = @Cid, gid = @Gid, name = @Name, surname = @Surname, gender = @Gender, age = @Age" +
                " where cid = @Cid", dbConnection);
            int children_id = Int32.Parse(textBoxChildrenId.Text);
            int group_id = Int32.Parse(textBoxGroupId.Text);
            //int position_id = Int32.Parse(textBoxName.Text);

            command.Parameters.Add("@Cid", SqlDbType.Int);
            command.Parameters["@Cid"].Value = children_id;

            command.Parameters.Add("@Gid", SqlDbType.Int);
            command.Parameters["@Gid"].Value = group_id;

            command.Parameters.Add("@Surname", SqlDbType.VarChar, 50);
            command.Parameters["@Surname"].Value = textBoxSurname.Text;

            command.Parameters.Add("@Name", SqlDbType.VarChar, 50);
            command.Parameters["@Name"].Value = textBoxName.Text;

            command.Parameters.Add("@Gender", SqlDbType.VarChar, 50);
            command.Parameters["@Gender"].Value = textBoxGender.Text;

            int age = Int32.Parse(textBoxAge.Text);
            command.Parameters.Add("@Age", SqlDbType.Int);
            command.Parameters["@Age"].Value = age;

            try
            {
                daChildren.UpdateCommand = command;
                int numberOfUpdatedChildren = daChildren.UpdateCommand.ExecuteNonQuery();
                if (numberOfUpdatedChildren != 0)
                {
                    ReloadChildrenTableView();
                }
                else
                {
                    MessageBox.Show("There is no children with the given id!");
                }
            }
            catch (SqlException sqlException)
            {
                if (sqlException.Number == 2627)
                    MessageBox.Show("The children id must be unique!");
                else if (sqlException.Number == 547)
                    MessageBox.Show("There's no group with the given id!");
                else
                    MessageBox.Show(sqlException.Message);
            }

        }
    }
}
