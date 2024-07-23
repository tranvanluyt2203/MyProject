import { isIOS } from '../utilies/Device'
export default {
    h0: isIOS() ? 28 : 26,
    h1: isIOS() ? 24 : 22,
    h2: isIOS() ? 22 : 20,
    h3: isIOS() ? 20 : 18,
    h4: isIOS() ? 18 : 16,
    h5: isIOS() ? 16 : 14,
    h6: isIOS() ? 14 : 12,
    h7: isIOS() ? 12 : 10,
    h8: isIOS() ? 10 : 8,
}