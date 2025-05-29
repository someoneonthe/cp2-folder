using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog85cForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(label1.Text);
            int num2 = (num1 - 165) / 100;
            int num3 = (num1 - 165) - (num2 * 100);
            label2.Text = num2.ToString() + "/" + num3.ToString();
        }
    }
}
