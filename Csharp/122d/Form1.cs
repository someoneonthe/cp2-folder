using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _122d
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int x = -12;
            while (x <= 16)
            {
                double y = Math.Pow(x, 6) - (3 * Math.Pow(x, 5)) - (93 * Math.Pow(x, 4)) + (87 * Math.Pow(x, 3)) + (1596 * Math.Pow(x, 2)) - (1380 * x) - 2800;
                listBox1.Items.Add(x + "\t" + y);
                x++;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
