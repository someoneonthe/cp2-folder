using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg535
{
    public partial class Form1 : Form
    {
        int Bob = 0;
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_MouseHover(object sender, EventArgs e)
        {
            Random rnd = new Random();
            int num = rnd.Next(1, 11);
            if (num == 1)
            {
                button1.Text = "Try Again";
            }
            if (num == 2)
            {
                button1.Text = "You're to slow";
            }
            if (num == 3)
            {
                button1.Text = "come on";
            }
            if (num == 4)
            {
                button1.Text = "Slowpoke";
            }
            if (num == 5)
            {
                button1.Text = "miss me";
            }
            if (num == 6)
            {
                button1.Text = "Hey Stinky";
            }
            if (num == 7)
            {
                button1.Text = "Poopyhead";
            }
            if (num == 8)
            {
                button1.Text = "No.";
            }
            if (num == 9)
            {
                button1.Text = "Nice Shot";
            }
            if (num == 10)
            {
                button1.Text = ":])))))))";
            }
            if (Bob == 1)
            {
                button1.Text = "you got me";
            }
            int he = rnd.Next(50, 300);
            int Le = rnd.Next(50, 300);
            button1.Left = Le;
            button1.Top = he;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bob = 1;
            
        }
    }
}
