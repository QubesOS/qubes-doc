PLANTUML_VER = 1.2020.0
PLANTUML_URL = https://downloads.sourceforge.net/project/plantuml/$(PLANTUML_VER)/plantuml.$(PLANTUML_VER).jar
PLANTUML_SHA256 = 7a9d2d56aeed9381066f98e3cf6450a06258ccfd4bfa7f306a62451e8af470c5

DIAGRAMS = qrexec-vm-dom0.png qrexec-dom0-vm.png qrexec-vm-vm.png

all: $(DIAGRAMS)

install:
	cp qrexec-vm-dom0.png ../doc/
	cp qrexec-dom0-vm.png ../doc/
	cp qrexec-vm-vm.png ../doc/

./%.png: %.uml $(PLANTUML)
	java -jar plantuml.jar $^

plantuml.jar:
	echo "PlantUML not found. Run 'make download'."

download:
	wget $(PLANTUML_URL) -O plantuml.$(PLANTUML_VER).jar.dl
	echo "$(PLANTUML_SHA256)  plantuml.$(PLANTUML_VER).jar.dl" | sha256sum -c
	mv plantuml.$(PLANTUML_VER).jar.dl plantuml.jar
