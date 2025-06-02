using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Final_Progect
{
    public partial class Form2 : Form
    {
        Form MyParent;
        public Form2(Form parent)
        {
            InitializeComponent();
            this.MyParent = parent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MyParent.Show();
            Hide();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            string path = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
            var lines = File.ReadAllLines(path + "/Password.txt");
            foreach (string line in lines)
            {
                var betaFileLine = System.Convert.FromBase64String(line);
                listBox1.Items.Add(System.Text.Encoding.UTF8.GetString(betaFileLine));
            }
        }
    }
}