#include <devenc/devicelist.h>

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2)
    {
      std::cerr << "Called with insufficient number of arguments. See manuals on how to call systemd generators\n";
      return -1;
    }

  QString path(argv[1]);
  QStringList dlist = DevEnc::DeviceList::instance()->devices();
  for (QString devid: dlist)
    {
      DevEnc::Device *device = DevEnc::DeviceList::instance()->device(devid);
      if (device && device->initialized())
        device->createSystemDConfig(path);
      else
        std::cout << "Device " << devid.toStdString() << " is not initialized";
    }

  return 0;
}
