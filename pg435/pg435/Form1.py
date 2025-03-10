
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(94, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(94, 43)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 31)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(94, 80)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 31)
		self._textBox3.TabIndex = 5
		self._textBox3.Text = "0.05"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(228, 25)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 40)
		self._button1.TabIndex = 7
		self._button1.Text = "Solve"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(228, 71)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 40)
		self._button2.TabIndex = 8
		self._button2.Text = "Back"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(76, 23)
		self._label1.TabIndex = 9
		self._label1.Text = "num of tickets"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 83)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(52, 23)
		self._label2.TabIndex = 10
		self._label2.Text = "tax"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Location = System.Drawing.Point(81, 151)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 11
		self._label3.Text = "label3"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 151)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(63, 23)
		self._label4.TabIndex = 12
		self._label4.Text = "total"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 43)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(76, 23)
		self._label5.TabIndex = 13
		self._label5.Text = "price"
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(334, 192)
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
		self.Name = "Form1"
		self.Text = "Form1"
		self.Load += self.Form1FormClosing
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		price = float(self._textBox2.Text)
		tax = float(self._textBox3.Text)
		ttax = tax + 1
		total = (num * price) * ttax
		self._label3.Text = str(total)

	def Form1FormClosing(self, sender, e):
		self.myparent.Show()

	def Button2Click(self, sender, e):
		self.myparent.Show()
		self.Close()

	def Label3Click(self, sender, e):
		self._label3.Text = "BOO"