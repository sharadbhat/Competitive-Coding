// LeetCode
// https://leetcode.com/problems/crawler-log-folder

package leetcode

func minOperations(logs []string) int {
	level := 0
	for _, command := range logs {
		if command == "../" && level > 0 {
			level--
		} else if command != "./" {
			level++
		}
	}
	return level
}
