import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._colorToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._redToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._greedToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._blueToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._blackToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._label1 = System.Windows.Forms.Label()
		self._toolStripMenuItem1 = System.Windows.Forms.ToolStripSeparator()
		self._CheckedVisible = System.Windows.Forms.ToolStripMenuItem()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._fileToolStripMenuItem,
			self._colorToolStripMenuItem,
			self._helpToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(284, 24)
		self._menuStrip1.TabIndex = 0
		self._menuStrip1.Text = "menuStrip1"
		# 
		# fileToolStripMenuItem
		# 
		self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._exitToolStripMenuItem]))
		self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
		self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 20)
		self._fileToolStripMenuItem.Text = "File"
		# 
		# exitToolStripMenuItem
		# 
		self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
		self._exitToolStripMenuItem.Size = System.Drawing.Size(92, 22)
		self._exitToolStripMenuItem.Text = "Exit"
		self._exitToolStripMenuItem.Click += self.ExitToolStripMenuItemClick
		# 
		# colorToolStripMenuItem
		# 
		self._colorToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._redToolStripMenuItem,
			self._greedToolStripMenuItem,
			self._blueToolStripMenuItem,
			self._blackToolStripMenuItem,
			self._toolStripMenuItem1,
			self._CheckedVisible]))
		self._colorToolStripMenuItem.Name = "colorToolStripMenuItem"
		self._colorToolStripMenuItem.Size = System.Drawing.Size(48, 20)
		self._colorToolStripMenuItem.Text = "Color"
		# 
		# helpToolStripMenuItem
		# 
		self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._aboutToolStripMenuItem]))
		self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
		self._helpToolStripMenuItem.Size = System.Drawing.Size(42, 20)
		self._helpToolStripMenuItem.Text = "help"
		# 
		# redToolStripMenuItem
		# 
		self._redToolStripMenuItem.Name = "redToolStripMenuItem"
		self._redToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._redToolStripMenuItem.Text = "Red"
		self._redToolStripMenuItem.Click += self.RedToolStripMenuItemClick
		# 
		# greedToolStripMenuItem
		# 
		self._greedToolStripMenuItem.Name = "greedToolStripMenuItem"
		self._greedToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._greedToolStripMenuItem.Text = "Green"
		self._greedToolStripMenuItem.Click += self.GreedToolStripMenuItemClick
		# 
		# blueToolStripMenuItem
		# 
		self._blueToolStripMenuItem.Name = "blueToolStripMenuItem"
		self._blueToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._blueToolStripMenuItem.Text = "Blue"
		self._blueToolStripMenuItem.Click += self.BlueToolStripMenuItemClick
		# 
		# blackToolStripMenuItem
		# 
		self._blackToolStripMenuItem.Name = "blackToolStripMenuItem"
		self._blackToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._blackToolStripMenuItem.Text = "Black"
		self._blackToolStripMenuItem.Click += self.BlackToolStripMenuItemClick
		# 
		# aboutToolStripMenuItem
		# 
		self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
		self._aboutToolStripMenuItem.Size = System.Drawing.Size(105, 22)
		self._aboutToolStripMenuItem.Text = "about"
		self._aboutToolStripMenuItem.Click += self.AboutToolStripMenuItemClick
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(29, 102)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(220, 89)
		self._label1.TabIndex = 1
		self._label1.Text = "The color in question"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# toolStripMenuItem1
		# 
		self._toolStripMenuItem1.Name = "toolStripMenuItem1"
		self._toolStripMenuItem1.Size = System.Drawing.Size(149, 6)
		# 
		# CheckedVisible
		# 
		self._CheckedVisible.Checked = True
		self._CheckedVisible.CheckOnClick = True
		self._CheckedVisible.CheckState = System.Windows.Forms.CheckState.Checked
		self._CheckedVisible.Name = "CheckedVisible"
		self._CheckedVisible.Size = System.Drawing.Size(152, 22)
		self._CheckedVisible.Text = "visible"
		self._CheckedVisible.Click += self.CheckedVisibleClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "pgMenuDemo"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def ExitToolStripMenuItemClick(self, sender, e):
		Application.Exit()

	def RedToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Red

	def GreedToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Green

	def BlueToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Blue

	def BlackToolStripMenuItemClick(self, sender, e):
		self._label1.ForeColor = Color.Black

	def AboutToolStripMenuItemClick(self, sender, e):
		MessageBox.Show("pizza test")

	def CheckedVisibleClick(self, sender, e):
		if self._CheckedVisible.Checked == True:
			self._label1.Visible = True
		else:
			self._label1.Visible = False