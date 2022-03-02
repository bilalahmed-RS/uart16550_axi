import os

from migen import *

#from litex import get_data_mod
from litex.soc.interconnect import axi
from litex.soc.integration.soc import *
from litex.soc.integration.doc import AutoDoc, ModuleDoc
from litex.soc.integration.soc import SoCRegion


class Open(Signal): pass
class RTL2UART(Module, AutoDoc, AutoCSR):
    """Verilog RTL-based UART 16550"""
    def __init__(self, platform, pads, default_enable=0):
        self.intro = ModuleDoc("""RTL2UART: A verilog RTL-based UART 16550 derived from the OpenCores.""")


        self.bus  = bus = axi_lite.Interface(data_width=32)
        self.s_axi_aclk = ClockSignal()
        self.s_axi_aresetn = ResetSignal()
        self.s_axi_awvalid = Signal()
        self.s_axi_awaddr = Signal(5)
        self.s_axi_awprot = Signal(3)
        self.s_axi_awready = Signal()
        self.s_axi_wvalid = Signal()
        self.s_axi_wdata = Signal(32)
        self.s_axi_wstrb = Signal(4)
        self.s_axi_wready = Signal()
        self.s_axi_bvalid = Signal()
        self.s_axi_bresp = Signal(2)
        self.s_axi_bready = Signal()
        self.s_axi_arvalid = Signal()
        self.s_axi_araddr = Signal(5)
        self.s_axi_arprot = Signal(3)
        self.s_axi_arready = Signal()
        self.s_axi_rvalid = Signal()
        self.s_axi_rdata = Signal(32)
        self.s_axi_rresp = Signal(2)
        self.s_axi_rready = Signal()
        self.int_o = Signal()
        self.srx_pad_i = Signal()
        self.stx_pad_o = Signal()
        self.rts_pad_o = Signal()
        self.cts_pad_i = Signal()
        self.dtr_pad_o = Signal()
        self.dsr_pad_i = Signal()
        self.ri_pad_i = Signal()
        self.dcd_pad_i = Signal()

        # # #

        self.specials += Instance("axi4lite_uart_top",
            i_s_axi_aclk=self.s_axi_aclk,
            i_s_axi_aresetn=self.s_axi_aresetn,
            i_s_axi_awvalid=self.s_axi_awvalid,
            i_s_axi_awaddr=self.s_axi_awaddr,
            i_s_axi_awprot=self.s_axi_awprot,
            o_s_axi_awready=self.s_axi_awready,
            i_s_axi_wvalid=self.s_axi_wvalid,
            i_s_axi_wdata=self.s_axi_wdata,
            i_s_axi_wstrb=self.s_axi_wstrb,
            o_s_axi_wready=self.s_axi_wready,
            o_s_axi_bvalid=self.s_axi_bvalid,
            o_s_axi_bresp=self.s_axi_bresp,
            i_s_axi_bready=self.s_axi_bready,
            i_s_axi_arvalid=self.s_axi_arvalid,
            i_s_axi_araddr=self.s_axi_araddr,
            i_s_axi_arprot=self.s_axi_arprot,
            o_s_axi_arready=self.s_axi_arready,
            o_s_axi_rvalid=self.s_axi_rvalid,
            o_s_axi_rdata=self.s_axi_rdata,
            o_s_axi_rresp=self.s_axi_rresp,
            i_s_axi_rready=self.s_axi_rready,
            o_int_o=self.int_o,
            i_srx_pad_i=self.srx_pad_i,
            o_stx_pad_o=self.stx_pad_o,
            o_rts_pad_o=self.rts_pad_o,
            i_cts_pad_i=self.cts_pad_i,
            o_dtr_pad_o=self.dtr_pad_o,
            i_dsr_pad_i=self.dsr_pad_i,
            i_ri_pad_i=self.ri_pad_i,
            i_dcd_pad_i=self.dcd_pad_i,
        )
        platform.add_source("/home/users/bilal.ahmed/litex_dev/Uart16550_axi/Uart16550_axi/verilog/uart_defines.v")
        platform.add_source("/home/users/bilal.ahmed/litex_dev/Uart16550_axi/Uart16550_axi/verilog/timescale.v")
        platform.add_source_dir(path="/home/users/bilal.ahmed/litex_dev/Uart16550_axi/Uart16550_axi/verilog/")

