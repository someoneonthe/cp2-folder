using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg298
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0;
        private void button1_Click(object sender, EventArgs e)
        {
            
            // Calc gross pay and display
            int[] inthours = new int[intMAX_EMPLOYEES];
            int COUNT = 0;
            int EMPLOHOURS = 0;
            decimal EMPLAY = 0;

            for (COUNT = 0; COUNT < intMAX_EMPLOYEES; COUNT++)
                while (int.TryParse(
                    Interaction.ImputBox("Enter # of hours worked by emplayee " +
                    (COUNT + 1).ToString(), "Need Hours Worked"),
                    out EMPLOHOURS) == false)
                {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
        }
    }
}
