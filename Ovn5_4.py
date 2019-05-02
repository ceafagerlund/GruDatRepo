# Övning 5, uppgift 4 (VG-uppgift). Gru_dat, Alexander Fagerlund.
# Inspiration DFS från https://yourbasic.org/algorithms/graph/.

# Vi har en elev-klass där varje elev har fem attribut:
# * ett namn self.name av typ "int" (t.ex. plats i klasslistan),
# * en tillordnad uppgift self.task av typ "int" med värde 1 eller 2, och
# * en närhetslista self.neighbors  (som är en array) som innehåller ...
#   de elever eleven känner i nummerordning.
# * attributen self.OneFailed och self.TwoFailed som visar om tilldelningar av
#   uppgifter fungerar eller inte. De är Booleans och ställs in under
#   iterationen.


Class Student:
    """Help class for student."""
    self.name = 0   #läraren ställer in namnen vid instantiering
    self.task = None #ska ställas in under iterationen  i workCheck
    self.neighbors = someList   #läraren skriver in detta
    self.OneFailed = False
    self.TwoFailed = False
    
def DidItWork(Graph):
    """Main function to check if graph works."""
    TruthCheck = True
    _workCheckDFS(Graph,first student,TruthCheck)
    if TruthCheck has value False:
        print("The noble enterprise failed")
    else:
        print("SUCCESS!")

def _workCheckDFS(Graph,student,TruthCheck):
    """Help function to DFS search graph."""
    if student is already visited
        return        
    Mark student as visited.
    set student.task to 1   #provar första uppgiften
    for all neighbors to student:
        if student and some neighbor have task == 1:
           set student.OneFailed to True
           set student.task to 2    #provar andra uppgiften
        if student and some neighbor have task == 2:
           set student.TwoFailed to True
        if student.OneFailed and student.TwoFailed are True:    #ingen tilldelning gick
           set TruthCheck to False
    for all neighbors x of student (in numerical order of name attribute):
        DFS(Graph,x,TruthCheck)
    
