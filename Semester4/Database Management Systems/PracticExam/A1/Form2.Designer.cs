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
            this.dgvGroup = new System.Windows.Forms.DataGridView();
            this.labelGroups = new System.Windows.Forms.Label();
            this.dgvChild = new System.Windows.Forms.DataGridView();
            this.labelChildren = new System.Windows.Forms.Label();
            this.labelCid = new System.Windows.Forms.Label();
            this.labelGid = new System.Windows.Forms.Label();
            this.labelName = new System.Windows.Forms.Label();
            this.labelSurname = new System.Windows.Forms.Label();
            this.textBoxChildrenId = new System.Windows.Forms.TextBox();
            this.textBoxGroupId = new System.Windows.Forms.TextBox();
            this.textBoxSurname = new System.Windows.Forms.TextBox();
            this.textBoxName = new System.Windows.Forms.TextBox();
            this.buttonRemove = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.labelGender = new System.Windows.Forms.Label();
            this.labelAge = new System.Windows.Forms.Label();
            this.textBoxGender = new System.Windows.Forms.TextBox();
            this.textBoxAge = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dgvGroup)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvGroup
            // 
            this.dgvGroup.AccessibleDescription = "";
            this.dgvGroup.AllowUserToAddRows = false;
            this.dgvGroup.AllowUserToDeleteRows = false;
            this.dgvGroup.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.dgvGroup.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvGroup.Location = new System.Drawing.Point(12, 40);
            this.dgvGroup.Name = "dgvGroup";
            this.dgvGroup.RowHeadersWidth = 70;
            this.dgvGroup.RowTemplate.Height = 30;
            this.dgvGroup.Size = new System.Drawing.Size(714, 407);
            this.dgvGroup.TabIndex = 0;
            this.dgvGroup.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgv_CellContentClick);
            this.dgvGroup.SelectionChanged += new System.EventHandler(this.GroupsView_SelectionChanged);
            // 
            // labelGroups
            // 
            this.labelGroups.AutoSize = true;
            this.labelGroups.Location = new System.Drawing.Point(13, 13);
            this.labelGroups.Name = "labelGroups";
            this.labelGroups.Size = new System.Drawing.Size(51, 16);
            this.labelGroups.TabIndex = 1;
            this.labelGroups.Text = "Groups";
            // 
            // dgvChild
            // 
            this.dgvChild.AllowUserToAddRows = false;
            this.dgvChild.AllowUserToDeleteRows = false;
            this.dgvChild.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.dgvChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvChild.Location = new System.Drawing.Point(732, 40);
            this.dgvChild.Name = "dgvChild";
            this.dgvChild.RowHeadersWidth = 51;
            this.dgvChild.RowTemplate.Height = 24;
            this.dgvChild.Size = new System.Drawing.Size(741, 407);
            this.dgvChild.TabIndex = 2;
            this.dgvChild.DataError += new System.Windows.Forms.DataGridViewDataErrorEventHandler(this.ChildrenView_DataError);
            this.dgvChild.SelectionChanged += new System.EventHandler(this.ChildrenView_SelectionChanged);
            // 
            // labelChildren
            // 
            this.labelChildren.AutoSize = true;
            this.labelChildren.Location = new System.Drawing.Point(729, 13);
            this.labelChildren.Name = "labelChildren";
            this.labelChildren.Size = new System.Drawing.Size(56, 16);
            this.labelChildren.TabIndex = 3;
            this.labelChildren.Text = "Children";
            this.labelChildren.Click += new System.EventHandler(this.labelEmployees_Click);
            // 
            // labelCid
            // 
            this.labelCid.AutoSize = true;
            this.labelCid.Location = new System.Drawing.Point(233, 472);
            this.labelCid.Name = "labelCid";
            this.labelCid.Size = new System.Drawing.Size(67, 16);
            this.labelCid.TabIndex = 4;
            this.labelCid.Text = "ChildrenId";
            // 
            // labelGid
            // 
            this.labelGid.AutoSize = true;
            this.labelGid.Location = new System.Drawing.Point(233, 509);
            this.labelGid.Name = "labelGid";
            this.labelGid.Size = new System.Drawing.Size(55, 16);
            this.labelGid.TabIndex = 5;
            this.labelGid.Text = "GroupId";
            // 
            // labelName
            // 
            this.labelName.AutoSize = true;
            this.labelName.Location = new System.Drawing.Point(233, 546);
            this.labelName.Name = "labelName";
            this.labelName.Size = new System.Drawing.Size(44, 16);
            this.labelName.TabIndex = 6;
            this.labelName.Text = "Name";
            // 
            // labelSurname
            // 
            this.labelSurname.AutoSize = true;
            this.labelSurname.Location = new System.Drawing.Point(233, 583);
            this.labelSurname.Name = "labelSurname";
            this.labelSurname.Size = new System.Drawing.Size(61, 16);
            this.labelSurname.TabIndex = 7;
            this.labelSurname.Text = "Surname";
            // 
            // textBoxChildrenId
            // 
            this.textBoxChildrenId.Location = new System.Drawing.Point(355, 472);
            this.textBoxChildrenId.Name = "textBoxChildrenId";
            this.textBoxChildrenId.Size = new System.Drawing.Size(333, 22);
            this.textBoxChildrenId.TabIndex = 8;
            // 
            // textBoxGroupId
            // 
            this.textBoxGroupId.Location = new System.Drawing.Point(355, 506);
            this.textBoxGroupId.Name = "textBoxGroupId";
            this.textBoxGroupId.Size = new System.Drawing.Size(333, 22);
            this.textBoxGroupId.TabIndex = 9;
            // 
            // textBoxSurname
            // 
            this.textBoxSurname.Location = new System.Drawing.Point(355, 580);
            this.textBoxSurname.Name = "textBoxSurname";
            this.textBoxSurname.Size = new System.Drawing.Size(333, 22);
            this.textBoxSurname.TabIndex = 10;
            // 
            // textBoxName
            // 
            this.textBoxName.Location = new System.Drawing.Point(355, 543);
            this.textBoxName.Name = "textBoxName";
            this.textBoxName.Size = new System.Drawing.Size(333, 22);
            this.textBoxName.TabIndex = 11;
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
            // labelGender
            // 
            this.labelGender.AutoSize = true;
            this.labelGender.Location = new System.Drawing.Point(233, 619);
            this.labelGender.Name = "labelGender";
            this.labelGender.Size = new System.Drawing.Size(52, 16);
            this.labelGender.TabIndex = 15;
            this.labelGender.Text = "Gender";
            // 
            // labelAge
            // 
            this.labelAge.AutoSize = true;
            this.labelAge.Location = new System.Drawing.Point(245, 657);
            this.labelAge.Name = "labelAge";
            this.labelAge.Size = new System.Drawing.Size(32, 16);
            this.labelAge.TabIndex = 16;
            this.labelAge.Text = "Age";
            // 
            // textBoxGender
            // 
            this.textBoxGender.Location = new System.Drawing.Point(355, 619);
            this.textBoxGender.Name = "textBoxGender";
            this.textBoxGender.Size = new System.Drawing.Size(333, 22);
            this.textBoxGender.TabIndex = 17;
            // 
            // textBoxAge
            // 
            this.textBoxAge.Location = new System.Drawing.Point(355, 657);
            this.textBoxAge.Name = "textBoxAge";
            this.textBoxAge.Size = new System.Drawing.Size(333, 22);
            this.textBoxAge.TabIndex = 18;
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1485, 697);
            this.Controls.Add(this.textBoxAge);
            this.Controls.Add(this.textBoxGender);
            this.Controls.Add(this.labelAge);
            this.Controls.Add(this.labelGender);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonRemove);
            this.Controls.Add(this.textBoxName);
            this.Controls.Add(this.textBoxSurname);
            this.Controls.Add(this.textBoxGroupId);
            this.Controls.Add(this.textBoxChildrenId);
            this.Controls.Add(this.labelSurname);
            this.Controls.Add(this.labelName);
            this.Controls.Add(this.labelGid);
            this.Controls.Add(this.labelCid);
            this.Controls.Add(this.labelChildren);
            this.Controls.Add(this.dgvChild);
            this.Controls.Add(this.labelGroups);
            this.Controls.Add(this.dgvGroup);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgvGroup)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvGroup;
        private System.Windows.Forms.Label labelGroups;
        private System.Windows.Forms.DataGridView dgvChild;
        private System.Windows.Forms.Label labelChildren;
        private System.Windows.Forms.Label labelCid;
        private System.Windows.Forms.Label labelGid;
        private System.Windows.Forms.Label labelName;
        private System.Windows.Forms.Label labelSurname;
        private System.Windows.Forms.TextBox textBoxChildrenId;
        private System.Windows.Forms.TextBox textBoxGroupId;
        private System.Windows.Forms.TextBox textBoxSurname;
        private System.Windows.Forms.TextBox textBoxName;
        private System.Windows.Forms.Button buttonRemove;
        private System.Windows.Forms.Button buttonUpdate;
        private System.Windows.Forms.Button buttonAdd;
        private System.Windows.Forms.Label labelGender;
        private System.Windows.Forms.Label labelAge;
        private System.Windows.Forms.TextBox textBoxGender;
        private System.Windows.Forms.TextBox textBoxAge;
    }
}