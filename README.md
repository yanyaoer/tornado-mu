本地域名
---

  brew install dnsmasq
  cp /usr/local/Cellar/dnsmasq/{VERSION}/dnsmasq.conf.example /usr/local/etc/dnsmasq.conf
  echo 'server=/dev/127.0.0.1' >> /etc/dnsmasq.conf
  echo "nameserver 127.0.0.1" | cat - /etc/resolv.conf > /etc/resolv.conf


添加站点
---

'''
  tornado-MU.git
  ├── base 
  ├── domain__tld 
  │   ├── static
  │   └── tpl
  └── domain2__tld 
      ├── static
      └── tpl
'''
