class Solution {
    encode(strs) {
        let encoded = "";

        for (const str of strs) {
            encoded += str.length + "#" + str;
        }

        return encoded;
    }

    decode(s) {
        const decoded = [];
        let i = 0;

        while (i < s.length) {
            let j = i;

            // Find the '#'
            while (s[j] !== "#") {
                j++;
            }

            // Length of the string
            const length = parseInt(s.substring(i, j));

            // Move past '#'
            j++;

            // Extract the string
            decoded.push(s.substring(j, j + length));

            // Move to the next encoded string
            i = j + length;
        }

        return decoded;
    }
}