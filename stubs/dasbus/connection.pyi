from typing import Callable, Optional

from dasbus.typing import Variant


class _InterfaceThing:
    def connect(self, callback: Callable[[str, list[str]], None]) -> None: ...


class _Signal:
    @staticmethod
    def connect(callback: Callable[[object, object, object], None]) -> None: ...
    @staticmethod
    def disconnect(callback: Callable[[object, object, object], None]) -> None: ...


class InterfaceProxy:
    Alias: str
    Connected: bool
    Discoverable: bool
    DiscoverableTimeout: int
    Discovering: bool
    InterfacesAdded: _InterfaceThing
    InterfacesRemoved: _InterfaceThing
    Name: str
    Powered: bool
    PropertiesChanged = _Signal
    SocketPathCtrl: str
    SocketPathIntr: str
    Trusted: bool
    Version: str

    def CancelPairing(self) -> None: ...
    def Connect(self) -> None: ...
    def Disconnect(self) -> None: ...
    def GetManagedObjects(self) -> dict[str, dict[str, dict[str, Variant[object]]]]: ...
    def Pair(self) -> None: ...
    def RegisterAgent(self, path: str, action: str) -> None: ...
    def RemoveDevice(self, path: str) -> None: ...
    def RequestDefaultAgent(self, path: str) -> None: ...
    def StartDiscovery(self) -> None: ...
    def StopDiscovery(self) -> None: ...


class SystemMessageBus:
    def get_proxy(self, service_name: str, object_path: str, interface_name: str) -> InterfaceProxy: ...
    def publish_object(self, object_path: str, obj: object) -> None: ...
