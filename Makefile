BUILDDIR=build
TARGET=$(BUILDIR)/rapport_proba.pdf

all: $(TARGET)

$(TARGET):
	@mkdir -p $(BUILDDIR)/
	pdflatex -output-directory=$(BUILDDIR) rapport_proba.tex
