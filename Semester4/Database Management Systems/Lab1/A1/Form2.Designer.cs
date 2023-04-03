namespace A1
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.StoresView = new System.Windows.Forms.DataGridView();
            this.labelStores = new System.Windows.Forms.Label();
            this.EmployeesView = new System.Windows.Forms.DataGridView();
            this.labelEmployees = new System.Windows.Forms.Label();
            this.labelEmid = new System.Windows.Forms.Label();
            this.labelStid = new System.Windows.Forms.Label();
            this.labelPoid = new System.Windows.Forms.Label();
            this.labelName = new System.Windows.Forms.Label();
            this.textBoxEmployeeId = new System.Windows.Forms.TextBox();
            this.textBoxStoreId = new System.Windows.Forms.TextBox();
            this.textBoxName = new System.Windows.Forms.TextBox();
            this.textBoxPositionId = new System.Windows.Forms.TextBox();
            this.buttonRemove = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonAdd = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.StoresView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.EmployeesView)).BeginInit();
            this.SuspendLayout();
            // 
            // StoresView
            // 
            this.StoresView.AllowUserToAddRows = false;
            this.StoresView.AllowUserToDeleteRows = false;
            this.StoresView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.StoresView.Location = new System.Drawing.Point(12, 40);
            this.StoresView.Name = "StoresView";
            this.StoresView.RowHeadersWidth = 70;
            this.StoresView.RowTemplate.Height = 30;
            this.StoresView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.StoresView.Size = new System.Drawing.Size(714, 407);
            this.StoresView.TabIndex = 0;
            this.StoresView.SelectionChanged += new System.EventHandler(this.StoresView_SelectionChanged);
            // 
            // labelStores
            // 
            this.labelStores.AutoSize = true;
            this.labelStores.Location = new System.Drawing.Point(13, 13);
            this.labelStores.Name = "labelStores";
            this.labelStores.Size = new System.Drawing.Size(46, 16);
            this.labelStores.TabIndex = 1;
            this.labelStores.Text = "Stores";
            // 
            // EmployeesView
            // 
            this.EmployeesView.AllowUserToAddRows = false;
            this.EmployeesView.AllowUserToDeleteRows = false;
            this.EmployeesView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.EmployeesView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.EmployeesView.Location = new System.Drawing.Point(732, 40);
            this.EmployeesView.Name = "EmployeesView";
            this.EmployeesView.RowHeadersWidth = 51;
            this.EmployeesView.RowTemplate.Height = 24;
            this.EmployeesView.Size = new System.Drawing.Size(741, 407);
            this.EmployeesView.TabIndex = 2;
            this.EmployeesView.SelectionChanged += new System.EventHandler(this.EmployeesView_SelectionChanged);
            this.EmployeesView.DataError += new System.Windows.Forms.DataGridViewDataErrorEventHandler(this.EmployeesView_DataError);
            // 
            // labelEmployees
            // 
            this.labelEmployees.AutoSize = true;
            this.labelEmployees.Location = new System.Drawing.Point(729, 13);
            this.labelEmployees.Name = "labelEmployees";
            this.labelEmployees.Size = new System.Drawing.Size(76, 16);
            this.labelEmployees.TabIndex = 3;
            this.labelEmployees.Text = "Employees";
            // 
            // labelEmid
            // 
            this.labelEmid.AutoSize = true;
            this.labelEmid.Location = new System.Drawing.Point(233, 472);
            this.labelEmid.Name = "labelEmid";
            this.labelEmid.Size = new System.Drawing.Size(80, 16);
            this.labelEmid.TabIndex = 4;
            this.labelEmid.Text = "EmployeeId";
            // 
            // labelStid
            // 
            this.labelStid.AutoSize = true;
            this.labelStid.Location = new System.Drawing.Point(233, 509);
            this.labelStid.Name = "labelStid";
            this.labelStid.Size = new System.Drawing.Size(50, 16);
            this.labelStid.TabIndex = 5;
            this.labelStid.Text = "StoreId";
            // 
            // labelPoid
            // 
            this.labelPoid.AutoSize = true;
            this.labelPoid.Location = new System.Drawing.Point(233, 546);
            this.labelPoid.Name = "labelPoid";
            this.labelPoid.Size = new System.Drawing.Size(66, 16);
            this.labelPoid.TabIndex = 6;
            this.labelPoid.Text = "PositionId";
            // 
            // labelName
            // 
            this.labelName.AutoSize = true;
            this.labelName.Location = new System.Drawing.Point(233, 583);
            this.labelName.Name = "labelName";
            this.labelName.Size = new System.Drawing.Size(44, 16);
            this.labelName.TabIndex = 7;
            this.labelName.Text = "Name";
            // 
            // textBoxEmployeeId
            // 
            this.textBoxEmployeeId.Location = new System.Drawing.Point(355, 472);
            this.textBoxEmployeeId.Name = "textBoxEmployeeId";
            this.textBoxEmployeeId.Size = new System.Drawing.Size(333, 22);
            this.textBoxEmployeeId.TabIndex = 8;
            // 
            // textBoxStoreId
            // 
            this.textBoxStoreId.Location = new System.Drawing.Point(355, 506);
            this.textBoxStoreId.Name = "textBoxStoreId";
            this.textBoxStoreId.Size = new System.Drawing.Size(333, 22);
            this.textBoxStoreId.TabIndex = 9;
            // 
            // textBoxName
            // 
            this.textBoxName.Location = new System.Drawing.Point(355, 580);
            this.textBoxName.Name = "textBoxName";
            this.textBoxName.Size = new System.Drawing.Size(333, 22);
            this.textBoxName.TabIndex = 10;
            // 
            // textBoxPositionId
            // 
            this.textBoxPositionId.Location = new System.Drawing.Point(355, 543);
            this.textBoxPositionId.Name = "textBoxPositionId";
            this.textBoxPositionId.Size = new System.Drawing.Size(333, 22);
            this.textBoxPositionId.TabIndex = 11;
            // 
            // buttonRemove
            // 
            this.buttonRemove.Location = new System.Drawing.Point(1017, 472);
            this.buttonRemove.Name = "buttonRemove";
            this.buttonRemove.Size = new System.Drawing.Size(201, 127);
            this.buttonRemove.TabIndex = 12;
            this.buttonRemove.Text = "Remove";
            this.buttonRemove.UseVisualStyleBackColor = true;
            this.buttonRemove.Click += new System.EventHandler(this.removeButton_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(1251, 472);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(193, 127);
            this.buttonUpdate.TabIndex = 13;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(805, 472);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(188, 130);
            this.buttonAdd.TabIndex = 14;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.addButton_Click);
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1485, 623);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonRemove);
            this.Controls.Add(this.textBoxPositionId);
            this.Controls.Add(this.textBoxName);
            this.Controls.Add(this.textBoxStoreId);
            this.Controls.Add(this.textBoxEmployeeId);
            this.Controls.Add(this.labelName);
            this.Controls.Add(this.labelPoid);
            this.Controls.Add(this.labelStid);
            this.Controls.Add(this.labelEmid);
            this.Controls.Add(this.labelEmployees);
            this.Controls.Add(this.EmployeesView);
            this.Controls.Add(this.labelStores);
            this.Controls.Add(this.StoresView);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);
            ((System.ComponentModel.ISupportInitialize)(this.StoresView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.EmployeesView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView StoresView;
        private System.Windows.Forms.Label labelStores;
        private System.Windows.Forms.DataGridView EmployeesView;
        private System.Windows.Forms.Label labelEmployees;
        private System.Windows.Forms.Label labelEmid;
        private System.Windows.Forms.Label labelStid;
        private System.Windows.Forms.Label labelPoid;
        private System.Windows.Forms.Label labelName;
        private System.Windows.Forms.TextBox textBoxEmployeeId;
        private System.Windows.Forms.TextBox textBoxStoreId;
        private System.Windows.Forms.TextBox textBoxName;
        private System.Windows.Forms.TextBox textBoxPositionId;
        private System.Windows.Forms.Button buttonRemove;
        private System.Windows.Forms.Button buttonUpdate;
        private System.Windows.Forms.Button buttonAdd;
    }
}