from generic_class import GenericClass
from capitalize_words import capitalize_words

generic_instance = GenericClass()

generic_instance.random_sentence = "Some random stuff with normal capilization"

generic_instance.capitalized_words_sentence = capitalize_words(
    generic_instance.random_sentence)

print("The original generic_instance.random_sentence")
print(generic_instance.random_sentence)

print("\nThe capitalized version generic_instance.capitalized_words_sentence: " +
      "capitalize_words(generic_instance.random_sentence)")
print(generic_instance.capitalized_words_sentence)
