
import text_compress
import random
import string

if __name__ == "__main__":
    #change this to affect what key set you're using to generate random strings
    test_key = string.ascii_letters


    passed = 0
    failed = 0
    comp = []
    minc, maxc = 1, 0
    for i in range(1000):
        test = ""
        for j in range(random.randint(50, 100)):
            test += test_key[random.randint(1, len(test_key)) - 1]

        key = text_compress.gen_key(test)
        compressed = text_compress.compress(test, key)
        uncompressed = text_compress.extract(compressed, key)

        result = "Pass: {0}, Compression {1}%, Original Size {2}, Compressed Size {3}, Uncompressed Size {4}".format(
            test == uncompressed,
            round(100 * len(compressed) / len(uncompressed), 2),
            len(test),
            len(compressed),
            len(uncompressed))
        #print(result)

        c = len(compressed) / len(uncompressed)
        comp.append(c)
        if c < minc:
            minc = c
        if c > maxc:
            maxc = c

        if test == uncompressed:
            passed += 1
        else:
            failed += 1

    print("Passed: {0}, Failed {1}, Average compression {2}, Min comp: {3}, Max comp: {4}".format(
        passed, failed, sum(comp) / len(comp), minc, maxc))