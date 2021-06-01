=begin
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
=end

@map = {}
def get_rand
    rand = ""
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    6.times do
        rand += alphabet[rand(alphabet.length)]
    end
    
    return rand
end

# Encodes a URL to a shortened URL.
#
# @param {string} longUrl
# @return {string}
def encode(longUrl)
    key = get_rand()
    while @map[key]
        key = get_rand()
    end
    @map[key] = longUrl
    
    return "http://tinyurl.com/#{key}"
end

# Decodes a shortened URL to its original URL.
#
# @param {string} shortUrl
# @return {string}
def decode(shortUrl)
    key = shortUrl.gsub("http://tinyurl.com/", "")
    return @map[key]
end


# Your functions will be called as such:
# decode(encode(url))