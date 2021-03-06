all:
	mkdir -p build/
	browserify pegaswitch/exploit/main.js > build/bundle.js || exit 1
	cp pegaswitch/exploit/minmain.js build/minmain.js || exit 2
	cp pegaswitch/exploit/index.html build/exploit.html || exit 3
	cp prebuilt/index.html build/index.html || exit 4
	cp prebuilt/cache build/cache || exit 5
	cp prebuilt/installer.nro build/installer.nro || exit 6
	cp prebuilt/rop.bin build/rop.bin || exit 7
	cp prebuilt/rop_relocs.bin build/rop_relocs.bin || exit 8

dev:
	cp ../nx-hbl/installer_obf/installer_obf.nro prebuilt/installer.nro || exit 9
	cp ../nx-hbl/runner_obf/build/rop.bin prebuilt/rop.bin || exit 10
	cp ../nx-hbl/runner_obf/build/rop_relocs.bin prebuilt/rop_relocs.bin || exit 11

clean:
	rm -rf build/

install:
	make -C pegaswitch install

deploy:
	scp -r build/* qlutoo@mtheall.com:pub_html/
