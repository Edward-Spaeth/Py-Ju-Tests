

myDict = {}

class Node:
	
	nodenumber = 0

	def __init__ (self, name):
		
		self.Name = name
		self.Predecessor = "Node cannot be Accessed"
		self.Distance = "Infinity"

		myDict [self.Name] = Node.nodenumber # Ordne dem Buchstaben einen Index zu (Hash)
		Node.nodenumber += 1



class Graph:


	def __init__ (self):
		
		self.Nodes = []
		self.Edges = []

	def addNodes (self, Nodearray):
		
		while (len (Nodearray) > 0):
			
			if myDict.get (Nodearray [0]) is None: # Wenn Knoten nicht bereits geaddet
				self.Nodes.append (Node (Nodearray [0]) )
			Nodearray = Nodearray [1:] # "Delete" First Element


	def BFS (self, Startknoten):

		#if myDict.get (Startknoten) is None:
			#print ("Der Startknoten existiert nicht")
			#return

		startindex = myDict.get (Startknoten)

		# myDict ist die Hashtabelle. "get" returned none wenn es den key Startknoten
		# nicht in der Hashtabelle gibt


		if startindex is None:
			print ("Der Startknoten", Startknoten, "existiert nicht")
			return

		self.Nodes [startindex].Predecessor = None
		self.Nodes [startindex].Distance = 0

		Q = []

		visitednodes = []

		visitednodes.append (Startknoten)



		Q.append (Startknoten)

		while Q:

			u = Q [0]
			Q = Q [1:]
			print (u, "wird gerade Besucht")
			
			for Start, Dest in self.Edges: # Start = Linker Teil des Paars, Dest = Rechter

				if Start == u:

					if Dest not in visitednodes:

						# get actual Objects with Names matching u and Dest
						u_node = self.Nodes [myDict [u] ]
						Dest_node = self.Nodes [myDict [Dest] ]

						# set Dest Values
						Dest_node.Predecessor = u_node.Name
						Dest_node.Distance = u_node.Distance + 1



						visitednodes.append (Dest)
						Q.append (Dest)

		print ("Die BFS Reihenfolge ist: ", visitednodes, "\n")


		for Node in self.Nodes:
			print ("Name:", Node.Name)
			print ("Predecessor:", Node.Predecessor)
			print ("Distance:", Node.Distance, "\n")











def main ():

	G = Graph ()

	Nodearray = ['A','B','C','D']

	Edgearray = [('A','C'), ('B', 'A'), ('B','C'), ('C', 'B')]

	G.addNodes (Nodearray)

	G.Edges = Edgearray

	G.BFS ('A') # Startknoten = 'A' (z.B)



if __name__ == "__main__":
	main ()
