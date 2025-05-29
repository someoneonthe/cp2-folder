using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = int.Parse(textBox1.Text);
            int points = 0;
            if (num == 1)
            {
                points = 5;
            }
            if (num == 2)
            {
                points = 15;
            }
            if (num == 3)
            {
                points = 30;
            }
            if (num >= 4)
            {
                points = 60;
            }
            label1.Text = "Points: " + points.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
