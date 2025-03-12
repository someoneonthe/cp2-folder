import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 78)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(224, 36)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(129, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(108, 31)
		self._textBox1.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Location = System.Drawing.Point(12, 47)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 28)
		self._label1.TabIndex = 2
		self._label1.Text = "paycheck:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Location = System.Drawing.Point(13, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(110, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "hour pay:"
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(15, 120)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 36)
		self._button2.TabIndex = 4
		self._button2.Text = "Erase"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(129, 120)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(108, 36)
		self._button3.TabIndex = 5
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ButtonShadow
		self.ClientSize = System.Drawing.Size(249, 163)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog122b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		pay = int(self._textBox1.Text) * 4
		self._label1.Text = "paycheck: " + str(pay)

	def Button2Click(self, sender, e):
		self._label1.Text = "paycheck:"
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
