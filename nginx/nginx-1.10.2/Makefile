
default:	build

clean:
	rm -rf Makefile objs

build:
	$(MAKE) -f objs/Makefile

install:
	$(MAKE) -f objs/Makefile install

modules:
	$(MAKE) -f objs/Makefile modules

upgrade:
	/root/CommercialWeb/nginx/nginx-install/sbin/nginx -t

	kill -USR2 `cat /root/CommercialWeb/nginx/nginx-install/logs/nginx.pid`
	sleep 1
	test -f /root/CommercialWeb/nginx/nginx-install/logs/nginx.pid.oldbin

	kill -QUIT `cat /root/CommercialWeb/nginx/nginx-install/logs/nginx.pid.oldbin`
