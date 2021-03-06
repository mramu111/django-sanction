.PHONY: test example tags cloc lint

# yes, i'm using cygwin atm.. don't judge me 
PKG_PATH=$(shell cygpath -u `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`)

test:
	nosetests -s --pdb --with-coverage --cover-package=django_sanction


example:
	cd example; \
	rm sql.db; \
	python manage.py syncdb --noinput; \
	python manage.py runserver 80


tags:
	ctags -R --python-kinds=-i --languages=python -f ./lib.tags $(PKG_PATH)
	ctags -R --python-kinds=-i --languages=python -f ./tags . 


cloc:
	cloc ./django_sanction --not-match-f=test.*


lint:
	pylint django_sanction --reports=n --include-ids=y


