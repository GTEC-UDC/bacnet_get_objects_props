# bacnet_get_objects_props

This repository includes the python script `bacnet_get_objects_props.py` (and the wrapper bash script `bacnet_get_objects_props.sh`) to obtain several properties of the BACnet objects of a BACnet device and save them into a CSV or a spreadsheet (.ods or .xlsx) file.

The [BAC0](https://github.com/ChristianTremblay/BAC0) library is used to obtain the BACnet data, and the [Pandas](https://pandas.pydata.org/) library is used to save the data to file.

An example of a CSV output is the following:

```csv
,device,device_id,name,type,type_value,address,description,units_state,simulated,overridden,priority_array,history_size,bacnet_properties
0,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Colec_Imp_Temp,analogValue,2,328,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
1,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Colec_Ret_Temp,analogValue,2,329,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
2,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Purgas_Volumen,analogValue,2,330,,cubicMeters,"(False, 0)","(False, 0)",,,{}
3,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Temp_Superior,analogValue,2,331,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
4,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Temp_Inferior,analogValue,2,332,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
5,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Diferencial,analogValue,2,333,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
6,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Consigna,analogValue,2,334,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
7,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Consigna_Legionella,analogValue,2,335,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
8,PABELLON_ELVINA,17,Pabellon_Elv_ACS_Deposito_Consigna_Efectiva,analogValue,2,336,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
9,PABELLON_ELVINA,17,Pabellon_Elv_Recup_P_Baja_Estado_BUS,analogInput,0,68,,noUnits,"(False, 0)","(False, 0)",,,{}
10,PABELLON_ELVINA,17,Pabellon_Elv_Recup_P_Baja_Temp_Ret,analogInput,0,69,,degreesCelsius,"(False, 0)","(False, 0)",,,{}
```
