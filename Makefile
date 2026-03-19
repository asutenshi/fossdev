create-practice:
	ifndef PRACTICE
	  $(error must pass val via PRACTICE)
	endif
		@echo "Creating practice"
		mkdir -p $(PRACTICE)

remove-practice:
	ifndef PRACTICE
	  $(error must pass val via PRACTICE)
	endif
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"

# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md