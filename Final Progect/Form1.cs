using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Final_Progect
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            form2 = new Form2(this);
            form3 = new Form3(this);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        public Form2 form2;
        public Form3 form3;
        private static string PasswordStuff = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=C:\Users\mullen.n\documents\visual studio 2013\Projects\Csharp\Final Progect\DataFiles\Passwords.mdf;Integrated Security=True";
        private void button3_Click(object sender, EventArgs e)
        {
            form2.Show();
            Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            form3.Show();
            Hide();
        }
    }
}
