import torch.nn as nn

class l2_distances(nn.Module):
    def __init__(self):
        super().__init__()
        self.mse = nn.MSELoss()


    def forward(self, pred_kpt, pred_distances, target_kpt, target_distances):
        mse1 = self.mse(pred_kpt,target_kpt)
        mse2 = self.mse(pred_distances,target_distances)
        return mse1+mse2

def load_loss(loss_name, class_weights=None, num_parts=None, printscreen=True, device=None):

    if printscreen:
        print('Using loss : %s..' % loss_name)

    if isinstance(loss_name, list):
        return [load_loss(l, class_weights=class_weights, num_parts=num_parts, printscreen=False, device=device) for l in loss_name]

    elif loss_name == 'L2':
        loss = nn.MSELoss()

    elif loss_name == 'L2_distances':
        loss = l2_distances()

    else:
        print('ERROR: loss name does not exist..')
        return

    return loss

