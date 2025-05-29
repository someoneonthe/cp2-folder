using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog54a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int miles = 0;
            int gallons = 0;
            double mpg = 0;
            if (comboBox1.Text == "1970 VW Bug")
            {
                miles = 286;
                gallons = 9;
            }
            else if (comboBox1.Text == "1979 Firebird")
            {
                miles = 412;
                gallons = 40;
            }
            else if (comboBox1.Text == "1980 Subru")
            {
                miles = 361;
                gallons = 18;
            }
            else if (comboBox1.Text == "1975 Cutlass")
            {
                miles = 161;
                gallons = 11;
            }
            else{
                MessageBox.Show("Invalid selection!");
                return;
            }
            mpg = (double)miles / gallons;
            mpg = Math.Round(mpg, 1);
            label6.Text = miles.ToString();
            label7.Text = gallons.ToString();
            label8.Text = mpg.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
