
"use strict";

let ActuatorControl = require('./ActuatorControl.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let Thrust = require('./Thrust.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let SysStatus = require('./SysStatus.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let RCIn = require('./RCIn.js');
let WaypointReached = require('./WaypointReached.js');
let Param = require('./Param.js');
let Tunnel = require('./Tunnel.js');
let PositionTarget = require('./PositionTarget.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let RTCM = require('./RTCM.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let DebugValue = require('./DebugValue.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let HilSensor = require('./HilSensor.js');
let LogData = require('./LogData.js');
let StatusText = require('./StatusText.js');
let ESCInfo = require('./ESCInfo.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let HilControls = require('./HilControls.js');
let Mavlink = require('./Mavlink.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let CommandCode = require('./CommandCode.js');
let TerrainReport = require('./TerrainReport.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let ExtendedState = require('./ExtendedState.js');
let RTKBaseline = require('./RTKBaseline.js');
let LogEntry = require('./LogEntry.js');
let RadioStatus = require('./RadioStatus.js');
let BatteryStatus = require('./BatteryStatus.js');
let VFR_HUD = require('./VFR_HUD.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let Vibration = require('./Vibration.js');
let HilGPS = require('./HilGPS.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let ParamValue = require('./ParamValue.js');
let HomePosition = require('./HomePosition.js');
let Trajectory = require('./Trajectory.js');
let ManualControl = require('./ManualControl.js');
let RCOut = require('./RCOut.js');
let CellularStatus = require('./CellularStatus.js');
let Waypoint = require('./Waypoint.js');
let State = require('./State.js');
let LandingTarget = require('./LandingTarget.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let Altitude = require('./Altitude.js');
let GPSINPUT = require('./GPSINPUT.js');
let GPSRAW = require('./GPSRAW.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let WaypointList = require('./WaypointList.js');
let MountControl = require('./MountControl.js');
let GPSRTK = require('./GPSRTK.js');
let VehicleInfo = require('./VehicleInfo.js');
let ESCStatus = require('./ESCStatus.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let FileEntry = require('./FileEntry.js');

module.exports = {
  ActuatorControl: ActuatorControl,
  OpticalFlowRad: OpticalFlowRad,
  TimesyncStatus: TimesyncStatus,
  ADSBVehicle: ADSBVehicle,
  Thrust: Thrust,
  OnboardComputerStatus: OnboardComputerStatus,
  CompanionProcessStatus: CompanionProcessStatus,
  SysStatus: SysStatus,
  CameraImageCaptured: CameraImageCaptured,
  RCIn: RCIn,
  WaypointReached: WaypointReached,
  Param: Param,
  Tunnel: Tunnel,
  PositionTarget: PositionTarget,
  ESCStatusItem: ESCStatusItem,
  WheelOdomStamped: WheelOdomStamped,
  RTCM: RTCM,
  MagnetometerReporter: MagnetometerReporter,
  ESCTelemetry: ESCTelemetry,
  DebugValue: DebugValue,
  AttitudeTarget: AttitudeTarget,
  HilSensor: HilSensor,
  LogData: LogData,
  StatusText: StatusText,
  ESCInfo: ESCInfo,
  ESCTelemetryItem: ESCTelemetryItem,
  HilControls: HilControls,
  Mavlink: Mavlink,
  OverrideRCIn: OverrideRCIn,
  CommandCode: CommandCode,
  TerrainReport: TerrainReport,
  EstimatorStatus: EstimatorStatus,
  GlobalPositionTarget: GlobalPositionTarget,
  ExtendedState: ExtendedState,
  RTKBaseline: RTKBaseline,
  LogEntry: LogEntry,
  RadioStatus: RadioStatus,
  BatteryStatus: BatteryStatus,
  VFR_HUD: VFR_HUD,
  ESCInfoItem: ESCInfoItem,
  Vibration: Vibration,
  HilGPS: HilGPS,
  CamIMUStamp: CamIMUStamp,
  PlayTuneV2: PlayTuneV2,
  ParamValue: ParamValue,
  HomePosition: HomePosition,
  Trajectory: Trajectory,
  ManualControl: ManualControl,
  RCOut: RCOut,
  CellularStatus: CellularStatus,
  Waypoint: Waypoint,
  State: State,
  LandingTarget: LandingTarget,
  NavControllerOutput: NavControllerOutput,
  Altitude: Altitude,
  GPSINPUT: GPSINPUT,
  GPSRAW: GPSRAW,
  HilStateQuaternion: HilStateQuaternion,
  WaypointList: WaypointList,
  MountControl: MountControl,
  GPSRTK: GPSRTK,
  VehicleInfo: VehicleInfo,
  ESCStatus: ESCStatus,
  HilActuatorControls: HilActuatorControls,
  FileEntry: FileEntry,
};
