"""Custom topology example



Two directly connected switches plus a host for each switch:



   host --- switch --- switch --- host



Adding the 'topos' dict with a key/value pair to generate our newly defined

topology enables one to pass in '--topo=mytopo' from the command line.

"""



from mininet.topo import Topo



class MyTopo( Topo ):

    "Simple topology example."



    def __init__( self ):

        "Create custom topo."



        # Initialize topology

        Topo.__init__( self )



        # Add hosts and switches

        Hostsatu = self.addHost( 'h1' )

        Hostdua = self.addHost( 'h2' )

	Hosttiga = self.addHost ( 'h3' )

	Hostempat = self.addHost ( 'h4' )

        Switchkiri = self.addSwitch( 's1' )

        Switchkanan = self.addSwitch( 's2' )

	Switchtengah = self.addSwitch( 's3' )


        # Add links

        self.addLink( Hostsatu, Switchkiri )
        self.addLink( Hostdua, Switchkiri )
        self.addLink( Hosttiga, Switchkanan )
        self.addLink( Hostempat, Switchkanan )
        self.addLink( Switchkiri, Switchtengah )
        self.addLink( Switchkanan, Switchtengah )


topos = { 'mytopo': ( lambda: MyTopo() ) }
