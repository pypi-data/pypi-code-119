from metadrive.component.pgblock.curve import Curve
from metadrive.component.pgblock.first_block import FirstPGBlock
from metadrive.component.road_network.node_road_network import NodeRoadNetwork
from metadrive.engine.asset_loader import initialize_asset_loader
from metadrive.tests.vis_block.vis_block_base import TestBlock

if __name__ == "__main__":
    test = TestBlock()

    initialize_asset_loader(test)

    global_network = NodeRoadNetwork()
    curve = FirstPGBlock(global_network, 3.0, 1, test.render, test.world, 1)
    for i in range(1, 13):
        curve = Curve(i, curve.get_socket(0), global_network, i)
        print(i)
        while True:
            success = curve.construct_block(test.render, test.world)
            print(success)
            if success:
                break
            curve.destruct_block(test.world)
    test.show_bounding_box(global_network)
    test.run()
