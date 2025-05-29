using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog54c
{
    public partial class Prog54bForm : Form
    {
        public Prog54bForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int num3 = int.Parse(textBox3.Text);
            int num4 = int.Parse(textBox4.Text);
            int sum = (num1 + num2 + num3 + num4) / 4;
            label1.Text = sum.ToString();
        }
    }
}
