class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
         const seen = new Set()

    for (let r=0; r < 9; r++) {
        for (let c=0; c < 9; c++) {
            const val = board[r][c]

            if (val == ".") continue

            const rb = Math.floor(r/3)
            const cb = Math.floor(c/3)

            const rowTag = `row${r}-val-${val}`
            const colTag = `col${c}-val-${val}`
            const boardTag = `board${rb}-${cb}-val-${val}`

            if(seen.has(rowTag) || seen.has(colTag) || seen.has(boardTag)) {
                return false
            }
            seen.add(rowTag)
            seen.add(colTag)
            seen.add(boardTag)


        }

    }
    return true
    }
}
