class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def helper(i, j):
            if i == j:
                return 1
            if i > j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            ans = 0
            if s[i] == s[j]:
                ans = max(ans, 2 + helper(i + 1, j - 1))
            else:
                ans = max(ans, helper(i, j - 1), helper(i + 1, j))
            dp[(i, j)] = ans
            return dp[(i, j)]

        return helper(0, len(s) - 1)

if __name__ == "__main__":
    x = "rqkkurdhcbzambxijfwsfxxrwtyhqacsgaxkzmsvodknqhfjfefxevffscridenwpczmzozaazzkyipeqjowkbifsloxkpinuwbiquigdvovkeyfjdtuiixyjqrtmbudjhkvzdhhkehbhcsvnlckmjgxjincbexvnrewofvibgcmzvrxmzszqnvxxvbwiadwkhxeswfrnwvezzpfdqdikhrjjdlomyqjhxynmfvpapevliwckvxosbrzdgmsvcyfqnzkhagtgqbibrzbnirokatylylxputxjpqdewzpanfyhbnnrbgcufqchooweuwrabgatlrcegvxkpaoqkanwxkycujgiqutjroyipqutohokxwzihbdxdpwcufktidkrzcrusokkbiimppvoeagpeucyhszmdgwqpluktdxqezghtjefikvezpwxcvnadhgwvxthanfzjlfgmatwmivpmbmlahdgubfosuksjjwwumrauhakhbfihhwfffknwswjqyffaeqhnccgdvrymyywiefbpunkhluvwjzjuhptdvaiokxypwtkzwixtllwghuscemqgvqqjoeiybuwptiscshxmbjsssasqddmanpjfyhihrkuhzipyimxuunrlkpnfkxvngtqikzmsyumutczippsljgltmabotqjrcdpyvmtlkaslqofvzdonlwjrsdpfofympbcfndwjdpccqjjzpjpontpmclzhipapqknfocdbrdmxlonbodcamtjgsvpvtzkazhxlhjccvcyihpirjzyhrgpxbtdmtdzynylievzbjdvuwmotsmnegnxyoghwjyxaqdynuwgzjzlsypgziinjytavwfmbcpvqtwtocozdwdoyezkselgdynjpuytbbwesvtaylhnoyczbkduiuptuqtwsnjhgmntvxrukdxmvrpuuaizxxgdxxojkilzpczuxdkahqjjoyhsgcvovppeplfbilkbrhvthzx"
    print(Solution().longestPalindromeSubseq(x))