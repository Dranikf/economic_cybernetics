class TreePoint():
    def __init__(self, index):
        self.matrix = [[1]];

    
    def init_brunches(self):
        self.brunches = [];
        brun_count = len(self.matrix);

        if brun_count == 1:
            return;

        for i in range(brun_count):
            self.brunches.append(TreePoint(i));
