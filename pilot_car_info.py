import obd

gas_level = 'loading...'
speed = 'loading...'
RPM = 'loading...'
eng_load = 'loading...'

def OBD_Grab(cmd):
  rsp = connection.query(cmd)
  valFromOBD = float(rsp.value.magnitude)
  return valFromOBD

def get_CarInfo():
  connection = obd.OBD('/dev/ttyUSB0')
  if 'connected' in str(connection.status()).lower():
    try:

      ELcmd = obd.commands.ENGINE_LOAD
      global eng_load
      eng_load= round(OBD_Grab(ELcmd), 2)

      FLcmd = obd.commands.FUEL_LEVEL
      global gas_level
      gas_level = round(OBD_Grab(FLcmd), 2)

      MPHcmd = obd.commands.SPEED
      global speed
      speed = round(int(OBD_Grab(MPHcmd)) * 0.6213712)

      RPMcmd = obd.commands.RPM
      global RPM
      RPM = int(OBD_Grab(RPMcmd))

      connection.close()

    except Exception as e:
      connection.close()
  else:
      pass
