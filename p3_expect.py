from expects import expect, be_above, be_below

value = 2 
expect(value).to(be_above(3)).and_to(be_below(10))
