class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
      for (int i = 0; i < 9; i++) {
        unordered_set<char> rowSet;
        unordered_set<char> colSet;
        unordered_set<char> boxSet;

        for (int j = 0; j < 9; j++) {
            // Check Rows
            if (board[i][j] != '.') {
                if (rowSet.count(board[i][j])) return false;
                rowSet.insert(board[i][j]);
            }

            // Check Columns
            if (board[j][i] != '.') {
                if (colSet.count(board[j][i])) return false;
                colSet.insert(board[j][i]);
            }

            // Check 3×3 Sub-Grids
            int row = 3 * (i / 3) + j / 3;  // Converts `i` into sub-grid row
            int col = 3 * (i % 3) + j % 3;  // Converts `j` into sub-grid column
            if (board[row][col] != '.') {
                if (boxSet.count(board[row][col])) return false;
                boxSet.insert(board[row][col]);
            }
        }
    }
    return true;
}
    
};
