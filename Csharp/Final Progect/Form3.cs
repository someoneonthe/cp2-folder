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
    public partial class Form3 : Form
    {
        public static object User;
        public static List <string> Full1 = new List <string>();
        Form MyParent;
        public Form3(Form parent)
        {
            InitializeComponent();
            this.MyParent = parent;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            MyParent.Show();
            Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string path = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
            string txt = textBox1.Text + "\t" + textBox2.Text + "\t" + textBox3.Text; Full1.Add(txt);
            using (StreamWriter sw = new StreamWriter(path + "/Password.txt",true))
            {
                sw.WriteLine(txt);
            }
        }
    }
}
