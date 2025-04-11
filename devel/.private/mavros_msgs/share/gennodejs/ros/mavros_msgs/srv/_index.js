
"use strict";

let FileRename = require('./FileRename.js')
let WaypointPush = require('./WaypointPush.js')
let FileRead = require('./FileRead.js')
let LogRequestList = require('./LogRequestList.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let ParamGet = require('./ParamGet.js')
let FileTruncate = require('./FileTruncate.js')
let WaypointPull = require('./WaypointPull.js')
let FileWrite = require('./FileWrite.js')
let MountConfigure = require('./MountConfigure.js')
let FileRemove = require('./FileRemove.js')
let CommandTOL = require('./CommandTOL.js')
let FileOpen = require('./FileOpen.js')
let FileChecksum = require('./FileChecksum.js')
let ParamPull = require('./ParamPull.js')
let SetMode = require('./SetMode.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let SetMavFrame = require('./SetMavFrame.js')
let ParamPush = require('./ParamPush.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let CommandBool = require('./CommandBool.js')
let MessageInterval = require('./MessageInterval.js')
let CommandHome = require('./CommandHome.js')
let LogRequestData = require('./LogRequestData.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandInt = require('./CommandInt.js')
let ParamSet = require('./ParamSet.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let FileClose = require('./FileClose.js')
let FileList = require('./FileList.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let CommandAck = require('./CommandAck.js')
let StreamRate = require('./StreamRate.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let WaypointClear = require('./WaypointClear.js')
let CommandLong = require('./CommandLong.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')

module.exports = {
  FileRename: FileRename,
  WaypointPush: WaypointPush,
  FileRead: FileRead,
  LogRequestList: LogRequestList,
  CommandTriggerControl: CommandTriggerControl,
  ParamGet: ParamGet,
  FileTruncate: FileTruncate,
  WaypointPull: WaypointPull,
  FileWrite: FileWrite,
  MountConfigure: MountConfigure,
  FileRemove: FileRemove,
  CommandTOL: CommandTOL,
  FileOpen: FileOpen,
  FileChecksum: FileChecksum,
  ParamPull: ParamPull,
  SetMode: SetMode,
  FileRemoveDir: FileRemoveDir,
  SetMavFrame: SetMavFrame,
  ParamPush: ParamPush,
  CommandVtolTransition: CommandVtolTransition,
  CommandBool: CommandBool,
  MessageInterval: MessageInterval,
  CommandHome: CommandHome,
  LogRequestData: LogRequestData,
  FileMakeDir: FileMakeDir,
  CommandInt: CommandInt,
  ParamSet: ParamSet,
  VehicleInfoGet: VehicleInfoGet,
  FileClose: FileClose,
  FileList: FileList,
  LogRequestEnd: LogRequestEnd,
  CommandAck: CommandAck,
  StreamRate: StreamRate,
  WaypointSetCurrent: WaypointSetCurrent,
  WaypointClear: WaypointClear,
  CommandLong: CommandLong,
  CommandTriggerInterval: CommandTriggerInterval,
};
