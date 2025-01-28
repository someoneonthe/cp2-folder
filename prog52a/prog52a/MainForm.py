import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Length"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Width"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 108)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Area"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 146)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(114, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Perimeter"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(119, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(119, 58)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 31)
		self._textBox2.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.Control
		self._label5.Location = System.Drawing.Point(119, 108)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.Control
		self._label6.Location = System.Drawing.Point(133, 146)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(86, 23)
		self._label6.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 32)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 210)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(82, 32)
		self._button2.TabIndex = 9
		self._button2.Text = "Erase"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(119, 210)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(62, 32)
		self._button3.TabIndex = 10
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(233, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		width = int(self._textBox2.Text)
		Height = int(self._textBox1.Text)
		Area = width * Height
		perimeter = (width * 2) + (Height * 2)
		self._label5.Text = str(Area)
		self._label6.Text = str(perimeter)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()