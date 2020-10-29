import dbus, dbus.mainloop.glib, sys
from gi.repository import GLib
import time

title = ''
album = ''
artist = ''

state = 'play'

def initMetadata():
    global player_iface
    while True:
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        obj = bus.get_object('org.bluez', "/")
        mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
        player_iface = None
        transport_prop_iface = None
        for path, ifaces in mgr.GetManagedObjects().items():
            if 'org.bluez.MediaPlayer1' in ifaces:
                player_iface = dbus.Interface(
                        bus.get_object('org.bluez', path),
                        'org.bluez.MediaPlayer1')
            elif 'org.bluez.MediaTransport1' in ifaces:
                transport_prop_iface = dbus.Interface(
                        bus.get_object('org.bluez', path),
                        'org.freedesktop.DBus.Properties')
        if not player_iface:
            time.sleep(1)
            continue
        if not transport_prop_iface:
            sys.exit('Error: DBus.Properties iface not found.')

        bus.add_signal_receiver(
            onMetadataUpdate,
            bus_name='org.bluez',
            signal_name='PropertiesChanged',
            dbus_interface='org.freedesktop.DBus.Properties')

        break
    GLib.MainLoop().run()

def mediaControl(new_state):
    global state
    if new_state == 'paused':
        player_iface.Pause()
        state = 'paused'
    elif new_state == 'play':
        player_iface.Play()
        state = 'play'
    elif new_state == 'last':
        player_iface.Previous()
        state = 'play'
    elif new_state == 'next':
        player_iface.Next()
        state = 'play'

def mediaGetState():
    return state

def onMetadataUpdate(interface, changed, invalidated):
    if interface != 'org.bluez.MediaPlayer1':
        return
    for prop, value in changed.items():
        if prop == 'Position':
            pass
        elif prop == 'Track':
            for key in ('Title', 'Artist', 'Album'):
               global title
               title = value.get('Title', '')
               global artist
               artist = value.get('Artist', '')
               global album
               album = value.get('Album', '')

if __name__ == "__main__":
    metaThr = threading.Thread(target=initMetadata, name = 'metadata')
    metaThr.start()
