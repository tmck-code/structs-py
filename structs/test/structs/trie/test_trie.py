from structs.trie.trie import Trie

class TestTrie:

    def test_insert(self):
        t = Trie()
        t.insert('cat')
        assert 'cat' in t
        assert 'car' not in t
        assert t['cat'].final

    def test_insert_with_data(self):
        t = Trie()
        t.insert('cat', 'feline')
        assert 'cat' in t
        assert t['cat'].data == ['feline']
        assert t['cat'].final
        assert str(t) == '''(root) -> {'c': c ([]) -> {'a': a ([]) -> {'t': t (['feline']) -> {}}}}'''

    def test_get_not_exist(self):
        t = Trie()
        t.insert('cat')
        err = None
        try:
            t['car']
        except Exception as e:
            err = e
        assert isinstance(err, KeyError)