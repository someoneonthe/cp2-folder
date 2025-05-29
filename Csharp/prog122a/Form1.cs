using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog122a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Number\tSquares\tSquare Root");
            int lcv = 1;
            while (lcv <= 50)
            {
                int sqr = (int) Math.Pow(lcv, 2);
                Double sqrt = Math.Sqrt(lcv);
                listBox1.Items.Add(lcv + "\t" + sqr + "\t" Math.Round(sqrt, 4));
                lcv++;
            }
        }
    }
}
