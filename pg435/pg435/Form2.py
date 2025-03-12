
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(17, 49)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(76, 23)
		self._label5.TabIndex = 23
		self._label5.Text = "price"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(17, 157)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(63, 23)
		self._label4.TabIndex = 22
		self._label4.Text = "total"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Location = System.Drawing.Point(86, 157)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 21
		self._label3.Text = "label3"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(17, 89)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(52, 23)
		self._label2.TabIndex = 20
		self._label2.Text = "tax"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(17, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(76, 23)
		self._label1.TabIndex = 19
		self._label1.Text = "num of tickets"
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(233, 77)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 40)
		self._button2.TabIndex = 18
		self._button2.Text = "Back"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(233, 31)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 40)
		self._button1.TabIndex = 17
		self._button1.Text = "Solve"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(99, 86)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 31)
		self._textBox3.TabIndex = 16
		self._textBox3.Text = "0.05"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(99, 49)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 31)
		self._textBox2.TabIndex = 15
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(99, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 14
		# 
		# Form2
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(346, 196)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "Form2"
		self.Text = "Form2"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Form1FormClosing(self, sender, e):
		self.myparent.Show()

	def Button2Click(self, sender, e):
		self.myparent.Show()
		self.Close()

	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		price = float(self._textBox2.Text)
		tax = float(self._textBox3.Text)
		ttax = tax + 1
		total = (num * price) * ttax
		self._label3.Text = str(total)