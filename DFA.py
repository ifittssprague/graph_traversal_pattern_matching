"""
Isaac Fitts-Sprague
Data Structures - ECE 241 - Project 3
12/18/2018
"""


from ArtistConnections import Vertex, Edge
from SongLibrary import SongLibrary


class DFA:

    def __init__(self, s=None):
        self.start = s

    """
    This function builds the DFA graph from the figure in the problem statement 
    """

    def build_DFA(self):

        # initiates all of the vertexes in the graph
        self.v0 = Vertex(0)
        self.start = self.v0
        self.v1 = Vertex(1)
        self.v2 = Vertex(2)
        self.v3 = Vertex(3)
        self.v4 = Vertex(4)
        self.v5 = Vertex(5)
        self.v6 = Vertex(6)
        self.v7 = Vertex(7)

        # sets the last vertex, V7, as the ending (accepting) vertex
        self.v7.setAcceptingState()

        # connects V0 to the other  vertexes
        self.v0.addEdge(Edge("A", self.v1))

        # connects V1 to the other  vertexes
        self.v1.addEdge(Edge("A", self.v1))
        self.v1.addEdge(Edge("C", self.v2))

        # connects V2 to the other  vertexes
        self.v2.addEdge(Edge("A", self.v3))

        # connects V3 to the other  vertexes
        self.v3.addEdge(Edge("C", self.v4))
        self.v3.addEdge(Edge("T", self.v1))

        # connects V4 to the other  vertexes
        self.v4.addEdge(Edge("A", self.v5))

        # connects V5 to the other  vertexes
        self.v5.addEdge(Edge("C", self.v4))
        self.v5.addEdge(Edge("T", self.v1))
        self.v5.addEdge(Edge("G", self.v6))

        # connects V6 to the other  vertexes
        self.v6.addEdge(Edge("A", self.v7))

        # connects V7 to the other  vertexes
        self.v7.addEdge(Edge("A", self.v1))
        self.v7.addEdge(Edge("C", self.v2))

        return

    """
    This function tests whether the input sequence seq will be accepted by the state machine
    It returns true if the input is accepted and false if not
    """

    def testMatch(self, seq):
        self.letters = list(seq)
        self.currentVert = self.v0

        # goes through all the letters in the list
        for letter in self.letters:
            # if the current vertex does not exist then it automatically fails and returns false

            if self.currentVert == None:
                return False

            self.currentVert = self.currentVert.followEdge(letter)

        if self.currentVert == None:
            return False

        # if it reaches the accepting state then its over and it returns true
        if self.currentVert.isAcceptingState == True:
            return True
        else:
            return False

        return False

    """
    This function tests whether the one suffix of the input sequence seq will be accepted by the state machine
    It retursn the index position of the suffix string if it is accepted, and returns -1 if its not accepted
    """

    def testAccept(self, seq):

        letters = list(seq)

        if len(letters) < 7:  # cannot be less than 7 letters so returns -1
            return -1

        elif len(letters) == 7:  # if its 7 letters then tests to see if its a match
            if self.testMatch(seq) == True:
                return 0
            else:
                return -1

        # when there are more than 7 letters
        else:
            # subStrList = [0] * len(letters)
            index = 0

            # while the length of the suffix to test is more than 7
            while len(letters) - index > 6:
                tempStr = ''.join(letters[index:])
                if self.testMatch(tempStr) == True:
                    return index
                index += 1

        return -1

    """
    This function goes through every song in the song library array and 
    tests whether they will be accepted by the state machine
    It stores the match index or -1 into the matchIndx array.
    """

    def testSongLibrary(self, song_lib):
        matchIndx = []

        for index in range(len(song_lib.songArray)):
            if song_lib.songArray == None:
                stop = 0
            matchIndx.append(self.testAccept(song_lib.songArray[index].DNA))  # stores the match index

        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    song_lib = SongLibrary()
    song_lib.loadLibrary()

    dfa = DFA()
    dfa.build_DFA()

    dfa.testSongLibrary(song_lib)
