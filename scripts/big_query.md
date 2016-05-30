#Big Query Script Notes

##Usage is printed by invoking the script without any parameters:

./big_query.py 
big_query.py: ip_address ascan 
      ip_address is the IP address of the BIG(Bluetooth Internet Gateway)
      ascan  specifies doing an active scan

## Logs of ascan 
XPS8700: ~/work/wiced/wiced_github.git/scripts : ./big_query.py 192.168.2.191 ascan
                                              href               bdaddr bdaddrType  rssi    (ADType, ADValue) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -45 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -56 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -66 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -66 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -55 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -55 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -51 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -52 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -61 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -61 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -64 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -64 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -52 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -52 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -41 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -61 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -64 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -41 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -45 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -64 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -64 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -59 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -61 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -61 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -53 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -54 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -44 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -62 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/425E791F18391         425E791F1839          1   -63 (1 1A)  (3 0A180D18)  (9 48656172742052617465) 
      http://192.168.2.191/gap/nodes/A4773345AE490         A4773345AE49          0   -82 (1 06)  (3 9FFE)  (22 9FFE026B68716C415861492D5A5100000154FF2CB2FA) 
      http://192.168.2.191/gap/nodes/A4773345AE490         A4773345AE49          0   -82 (1 06)  (3 9FFE)  (22 9FFE026B68716C415861492D5A5100000154FF2CB2FA) 
      http://192.168.2.191/gap/nodes/A477338B80B50         A477338B80B5          0   -53 (1 06)  (3 9FFE)  (22 9FFE02437848586E4255576B576F00000154FF2CB3A6) 
      http://192.168.2.191/gap/nodes/B034953DC1460         B034953DC146          0   -92 (1 1A)  (55 4C000906030AC0A80167) 
      http://192.168.2.191/gap/nodes/B034953DC1460         B034953DC146          0   -82 (1 1A)  (55 4C000906030AC0A80167) 
      http://192.168.2.191/gap/nodes/B034953DC1460         B034953DC146          0   -82 (1 1A)  (55 4C000906030AC0A80167) 
      http://192.168.2.191/gap/nodes/B034953DC1460         B034953DC146          0   -92 (1 1A)  (55 4C000906030AC0A80167) 